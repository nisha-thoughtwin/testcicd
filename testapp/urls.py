from django.contrib import admin
from django.urls import path


from .views import EmployeeCreateApi

urlpatterns = [
    path('api/create',EmployeeCreateApi.as_view(),name='employee_create'),
]