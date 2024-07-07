from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import viewsets, permissions
from .models import Company, Employee
from .serializers import EmployeeSerializer, CompanySerializer
from rest_framework.response import Response


class CompanyViewset(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def list(self, request):
        # Retrieve all instances of the model
        queryset = self.queryset
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        # Create a new instance of the model
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=404)

    def retrieve(self, request, pk=None):
        # Retrieve a specific instance of the model by primary key (pk)
        company = self.queryset.get(pk=pk)
        serializer = self.serializer_class(company)
        return Response(serializer.data)

    def update(self, request, pk=None):
        # Update a specific instance of the model by primary key (pk)
        company = self.queryset.get(pk=pk)
        serializer = self.serializer_class(company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=404)

    def destroy(self, request, pk=None):
        # Delete a specific instance of the model by primary key (pk)
        company = self.queryset.get(pk=pk)
        company.delete()
        return Response(status=204)


class EmployeeViewset(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def list(self, request):
        # Retrieve all instances of the model
        queryset = self.queryset
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        # Create a new instance of the model
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=404)

    def retrieve(self, request, pk=None):
        # Retrieve a specific instance of the model by primary key (pk)
        employee = self.queryset.get(pk=pk)
        serializer = self.serializer_class(employee)
        return Response(serializer.data)

    def update(self, request, pk=None):
        # Update a specific instance of the model by primary key (pk)
        employee = self.queryset.get(pk=pk)
        serializer = self.serializer_class(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=404)

    def destroy(self, request, pk=None):
        # Delete a specific instance of the model by primary key (pk)
        employee = self.queryset.get(pk=pk)
        employee.delete()
        return Response(status=204)
