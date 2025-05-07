from ops.employees.employee import Employee


def send_email(employee: Employee, message: str) -> None:
    """Email notificaiton implementation."""
    print(f"Sending email to {employee.name}: {message}")


def send_sms(employee: Employee, message: str) -> None:
    """SMS notification implementation."""
    print(f"Sending SMS to {employee.name}: {message}")
