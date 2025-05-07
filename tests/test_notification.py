import pytest
from ops.employees.employee import Employee
from ops.notifications.notification import send_email, send_sms


@pytest.fixture
def employee():
    return Employee(name="John Doe", role="developer")


def test_send_email(capsys, employee):
    message = "This is a test email."
    send_email(employee, message)
    captured = capsys.readouterr()
    assert f"Sending email to {employee.name}: {message}" in captured.out


def test_send_sms(capsys, employee):
    message = "This is a test SMS."
    send_sms(employee, message)
    captured = capsys.readouterr()
    assert f"Sending SMS to {employee.name}: {message}" in captured.out
