from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=20)
    registration_date = models.DateField()
    registration_number = models.CharField(max_length=12, unique=True)
    address = models.TextField()
    contact_person = models.CharField(max_length=100)
    contact_phone = models.IntegerField()
    list_of_departments = models.TextField()
    number_of_employees = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Employee(models.Model):
    employee_id = models.CharField(max_length=8, primary_key=True)
    name = models.CharField(max_length=50)
    contact_phone = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name="employees"
    )
    department = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    date_started = models.DateField()
    date_left = models.DateField(null=True, blank=True)
    duties = models.TextField()

    def __str__(self):
        return self.name
