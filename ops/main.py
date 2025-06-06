from company.company import Company
from employees.hourly import HourlyEmployee
from employees.salaried import SalariedEmployee
from notifications import notification


def main() -> None:
    """Main function."""

    company = Company()

    juniven = SalariedEmployee(name="Juniven", role="manager")
    company.add_employee(juniven)
    company.add_employee(HourlyEmployee(name="Ellen", role="president"))
    company.add_employee(HourlyEmployee(name="Prince", role="support"))

    print(company.find_by_role(role="president"))
    print(company.find_by_role(role="manager"))
    print(company.find_by_role(role="support"))
    company.pay_employee(company.employees[0])
    company.employees[0].take_a_single_holiday()

    notification.send_email(employee=juniven, message="Your leave request is approved.")


if __name__ == "__main__":
    main()
