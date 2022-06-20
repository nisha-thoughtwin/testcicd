from django.db import models

# Create your models here.
class Employee(models.Model):
  employee_regNo = models.IntegerField(unique=True)
  employee_name = models.CharField(max_length=100)
  employee_email = models.CharField(max_length=100)
  employee_mobile = models.IntegerField()
  employee_dob = models.DateField()
  # emplyee_age = models.IntegerField()
  created_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.employee_name

