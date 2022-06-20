from rest_framework import serializers
from django.utils import timezone
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    employee_email = serializers.EmailField(max_length=100,)
    
    created_at = serializers.DateTimeField(read_only=True, default=timezone.now)
    employee_dob = serializers.DateField()
    employee_name = serializers.CharField(max_length=100)
    employee_regNo = serializers.IntegerField()


    class Meta:
        model = Employee
        fields = ['employee_regNo','employee_name','employee_email','employee_mobile','employee_dob','created_at']