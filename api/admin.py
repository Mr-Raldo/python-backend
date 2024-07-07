from django.contrib import admin
from .models import Company, Employee
from django import forms

# Register your models here.


admin.site.register(Employee)
admin.site.register(Company)



