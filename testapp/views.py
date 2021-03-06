from django.shortcuts import render
from rest_framework import generics,viewsets
from .models import Employee
from testapp.serializers import EmployeeSerializer


# Create views here.
class EmployeeCreateApi(generics.CreateAPIView):
  queryset = Employee.objects.all()
  serializer_class = EmployeeSerializer
