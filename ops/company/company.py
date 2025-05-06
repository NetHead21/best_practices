from employees.employee import (
    Employee,
    HourlyEmployee,
    SalariedEmployee,
    Freelancer,
    Intern,
)


class Company:
    """Represents a company with employee."""

    def __init__(self) -> None:
        self.employees: list[Employee] = []

    def add_employee(self, employee: Employee) -> None:
        self.employees.append(employee)

    def find_managers(self) -> list[Employee]:
        return [e for e in self.employees if e.role == "manager"]

    def find_vice_presidents(self) -> list[Employee]:
        return [e for e in self.employees if e.role == "vice-president"]

    def find_support_staff(self) -> list[Employee]:
        return [e for e in self.employees if e.role == "support"]

    def pay_employee(self, employee: Employee) -> None:
        if isinstance(employee, SalariedEmployee):
            print(
                f"Paying employee {employee.name} a monthly salary of ${employee.monthly_salary}."
            )
        elif isinstance(employee, HourlyEmployee):
            print(
                f"Pyaing employee {employee.name} a hourly rate of ${employee.hourly_rate} for {employee.amount} hours."
            )
        elif isinstance(employee, Freelancer):
            print(
                f"Playing freelancer {employee.name} a hourly rate of ${employee.hourly_rate} for {employee.amount} hours."
            )
        elif isinstance(employee, Intern):
            print(
                f"Paying intern {employee.name} a monthly salary of ${employee.monthly_salary}"
            )
