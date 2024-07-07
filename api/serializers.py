from rest_framework import serializers

from .models import Company,  Employee


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"  # Alternatively, specify the fields explicitly: ['id', 'name', 'registration_date', 'registration_number', 'address', 'contact_person', 'departments', 'number_of_employees']




class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"  # Alternatively, specify the fields explicitly: ['employee_id', 'name', 'contact_phone', 'email', 'company', 'department', 'role', 'date_started', 'date_left', 'duties']
