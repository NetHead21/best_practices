from company.company import Company
from employees.employee import (
    HourlyEmployee,
    SalariedEmployee,
)
from notifications.notification import NotificationFactory


def main() -> None:
    """Main function."""

    company = Company()

    juniven = SalariedEmployee(name="Juniven", role="manager")
    company.add_employee(juniven)
    company.add_employee(HourlyEmployee(name="Ellen", role="president"))
    company.add_employee(HourlyEmployee(name="Prince", role="support"))

    print(company.find_vice_presidents())
    print(company.find_managers())
    print(company.find_support_staff())
    company.pay_employee(company.employees[0])
    company.employees[0].take_a_holiday(False)

    notification = NotificationFactory.get_notification("email")
    notification.send(employee=juniven, message="Your leave request is approved.")


if __name__ == "__main__":
    main()
