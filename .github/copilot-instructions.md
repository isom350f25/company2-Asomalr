## Quick context

This is a small Django monolith (Django 5.1.5) with a single app `compapp`. The app models employees (and a Project model appears in source) and renders simple, non-namespaced templates from `compapp/templates/`.

Key files to inspect when making changes:
- `companyproj/settings.py` — DB = SQLite (`db.sqlite3` at repo root), DEBUG=True, INSTALLED_APPS includes `compapp`.
- `companyproj/urls.py` — mounts the app at `path('comp/', include('compapp.urls'))`.
- `compapp/models.py` and `compapp/migrations/0001_initial.py` — canonical source of current DB schema (use migration when fields differ from models file).
- `compapp/views.py`, `compapp/urls.py` — view and URL entry points. Templates are referenced by filename (e.g. `'employee_list.html'`).

## Big-picture architecture

- Single Django project with one app `compapp`. No containers or external services configured.
- Persistent data: SQLite at repo root. Migrations are present; prefer running migrations rather than editing `db.sqlite3` directly.
- Templates are app-local and used directly because `TEMPLATES['APP_DIRS'] = True` (render uses simple names like `employee_list.html`).

## Developer workflows (explicit commands)

- Create/inspect/migrate DB (development):

  - Install dependencies (project does not include a requirements file; assume a Python venv with Django 5.1.5):
    python -m venv .venv; .\.venv\Scripts\Activate.ps1; pip install django==5.1.5

  - Make migrations and apply them:
    python companyproj\manage.py makemigrations
    python companyproj\manage.py migrate

  - Run dev server:
    python companyproj\manage.py runserver

  - Django admin is available at `/admin/` (admin app enabled in `settings.py`).

## Project-specific conventions and gotchas

- Single app monolith: changes to models, views and templates are colocated inside `companyproj/compapp/`.
- Migration file `compapp/migrations/0001_initial.py` is the authoritative snapshot of the existing DB schema. Use it to infer field names/types (e.g. `Employee` has `name`, `date_joined`, `date_of_birth`, `phone_number`, `position`).
- Templates are simple and sometimes incomplete; inspect `compapp/templates/employee_list.html` and `employee_detail.html` before editing.
- Current codebase contains duplicated and incomplete code (examples below). Prefer to clean up duplicates and missing imports rather than adding new duplicates.

Examples of discovered issues (be mindful when editing):
- `compapp/views.py` has two definitions of `employee_list` and uses `get_object_or_404` in `employee_detail` without importing it. Fixes should remove duplicates and add imports:

  from django.shortcuts import render, get_object_or_404

- `compapp/models.py` contains duplicated model definitions and stray HTML at the file end; use `migrations/0001_initial.py` as source of truth for the DB schema.

## Code-change guidance (how to make safe edits)

- When changing models:
  - Update `compapp/models.py`, run `makemigrations` and `migrate`.
  - Do not edit `db.sqlite3` directly.

- When changing templates:
  - Files live in `companyproj/compapp/templates/` and are referenced by name (no template namespace). Restart the dev server or let Django autoreload.

- URLs:
  - `companyproj/urls.py` mounts `compapp` under `/comp/`. So `compapp/urls.py` paths like `employees/` resolve to `/comp/employees/`.

## Tests and linters

- There are no tests or linter configs in the repo. If you add tests, place them in `compapp/tests.py` and run `python companyproj\manage.py test`.

## When opening PRs

- Include migrations for model changes and a short note describing DB shape changes.
- For UI fixes, include before/after screenshots where helpful and reference the specific template file(s) changed.

## Quick references (files to open first)
- `companyproj/settings.py` — configuration
- `compapp/models.py` and `compapp/migrations/0001_initial.py` — data model
- `compapp/views.py` and `compapp/urls.py` — controllers and endpoints
- `compapp/templates/employee_list.html`, `employee_detail.html` — UI

If anything in this file is unclear or you'd like additional examples (e.g., a recommended patch to fix the duplicate view + missing import), tell me which area to expand and I will update this document.
