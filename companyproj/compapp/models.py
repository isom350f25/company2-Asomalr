from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=100)
    date_joined = models.DateField()
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=8)
    position = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} - {self.position}"



from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    # add any other fields you have

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    extra_pay = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    employees = models.ManyToManyField(Employee, related_name='projects', blank=True)

    def __str__(self):
        return self.name
<h1>Employees</h1>

<ul>
  {% for employee in employees %}
    <li>
      <a href="{% url 'employee_detail' employee.pk %}">
        {{ employee.name }} ({{ employee.position }})
      </a>
    </li>
  {% endfor %}
</ul>
