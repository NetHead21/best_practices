from .employee import Employee
from dataclasses import dataclass


@dataclass
class SalariedEmployee(Employee):
    monthly_salary: float = 50000
