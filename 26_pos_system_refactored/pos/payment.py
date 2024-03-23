from pos.data import PaymentStatus
from typing import Callable, Protocol
from dataclasses import dataclass

AuthorizeFunction = Callable[[], bool]


class Payable(Protocol):
    @property
    def total_price(self) -> int:
        ...

    def set_payment_status(self, status: PaymentStatus) -> None:
        ...


class PaymentProcessor(Protocol):
    def pay(self, payable: Payable, authorize: AuthorizeFunction) -> None:
        ...


class DebitPaymentProcessor:
    def pay(self, payable: Payable, authorize: AuthorizeFunction) -> None:
        if not authorize():
            raise Exception("Not authorized")

        print(f"Processing debit payment for P{payable.total_price:.2f}")
        payable.set_payment_status(PaymentStatus.PAID)


@dataclass
class CreditPaymentProcessor:
    security_code: str

    def pay(self, payable: Payable, authorize: AuthorizeFunction) -> None:
        if not authorize():
            raise Exception("Not authorized")

        print(f"Processing credit payment for P{payable.total_price:.2f}")
        payable.set_payment_status(PaymentStatus.PAID)


@dataclass
class PayPalPaymentProcessor:
    email_address: str

    def pay(self, payable: Payable, authorize: AuthorizeFunction) -> None:
        if not authorize():
            raise Exception("Not authorized")

        print(
            f"Processing PayPal payment for amount: P{payable.total_price:.2f} \n Confirmation was sent to your email: {self.email_address}"
        )
        payable.set_payment_status(PaymentStatus.PAID)
