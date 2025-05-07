from .employee import Employee
from dataclasses import dataclass


@dataclass
class HourlyEmployee(Employee):
    hourly_rate: float = 50
    amount: int = 10
