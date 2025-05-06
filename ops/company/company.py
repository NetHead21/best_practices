from employees.employee import (
    Employee,
    HourlyEmployee,
    SalariedEmployee,
)


class Company:
    """Represents a company with employee."""

    def __init__(self) -> None:
        self.employees: list[Employee] = []

    def add_employee(self, employee: Employee) -> None:
        self.employees.append(employee)

    def find_by_role(self, role: str) -> list[Employee]:
        return [e for e in self.employees if e.role == role]

    def pay_employee(self, employee: Employee) -> None:
        if isinstance(employee, SalariedEmployee):
            print(
                f"Paying employee {employee.name} a monthly salary of ${employee.monthly_salary}."
            )
        elif isinstance(employee, HourlyEmployee):
            print(
                f"Pyaing employee {employee.name} a hourly rate of ${employee.hourly_rate} for {employee.amount} hours."
            )
