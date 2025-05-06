from abc import ABC, abstractmethod


class Notification(ABC):
    """Abstract base class for notifications."""

    @abstractmethod
    def send(slef, employee: Employee, massage: str) -> None: ...


class EmailNotification(Notification):
    """Email notificaiton implementation."""

    def send(self, employee: Employee, message: str) -> None:
        print(f"Sending email to {employee.name}: {message}")


class SMSNotification(Notification):
    """SMS notification implementation."""

    def send(self, employee: Employee, message: str) -> None:
        print(f"Sending SMS to {employee.name}: {message}")


class NotificationFactory:
    """Factory for creating notifications."""

    @staticmethod
    def get_notification(method: str) -> Notification:
        if method == "email":
            return EmailNotification()
        elif method == "sms":
            return SMSNotifiction()
        else:
            raise ValueError("Invalid notification method")
