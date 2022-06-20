from django.urls import reverse
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

# Create your tests here.
class EmployeeTestCase(TestCase):
  def setUp(self):
    self.client = APIClient()
    self.employee_data =   {
        "employee_regNo": 103,
        "employee_name": "nisha",
        "employee_email": "nisha@gmail.com",
        "employee_mobile": 9644247764,
        "employee_dob": "1997-05-19",
        "created_at": "2021-05-29T13:05:59.551255Z"
    }
    self.response = self.client.post(
        reverse('employee_create'),
        self.employee_data,
        format="json")

  def test_01_api_can_create_a_employee(self):
    response=self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)