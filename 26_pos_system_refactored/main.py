from typing import Callable
from pos.order import LineItem, Order
from pos.payment import (
    AuthorizeFunction,
    PaymentProcessor,
    CreditPaymentProcessor,
    DebitPaymentProcessor,
    PayPalPaymentProcessor,
)
from pos.authorization import (
    authorize_google,
    authorize_robot,
    authorize_sms,
)

AUTHORIZERS: dict[str, AuthorizeFunction] = {
    "google": authorize_google,
    "robot": authorize_robot,
    "sms": authorize_sms,
}


def create_credit_processor() -> PaymentProcessor:
    security_code = input("Enter the security code: ")
    return CreditPaymentProcessor(security_code)


def create_debit_processor() -> PaymentProcessor:
    return DebitPaymentProcessor()


def create_paypal_processor() -> PaymentProcessor:
    email_address = input("Enter your email address: ")
    return PayPalPaymentProcessor(email_address)


PAYMENT_PROCESSORS: dict[str, Callable[[], PaymentProcessor]] = {
    "credit": create_credit_processor,
    "debit": create_debit_processor,
    "paypal": create_paypal_processor,
}


def read_choice(question: str, choices: list[str]) -> str:
    choice = ""
    while choice not in choices:
        choice = input(f"{question} ({', '.join(choices)})? ")
    return choice


def read_authorizer() -> AuthorizeFunction:
    auth_choice = read_choice("How would you like to pay?", list(AUTHORIZERS.keys()))
    return AUTHORIZERS[auth_choice]


def read_payment_processor() -> PaymentProcessor:
    payment_processor_choice = read_choice(
        "Using what payment option?", list(PAYMENT_PROCESSORS.keys())
    )
    return PAYMENT_PROCESSORS[payment_processor_choice]()


def main() -> None:
    order = Order()
    order.add_item(LineItem("Keyboard", 1, 1000))
    order.add_item(LineItem("SSD", 1, 5000))
    order.add_item(LineItem("USB Cable", 2, 500))

    print(f"The total Price is: P{order.total_price:.2f}")

    authorizer = read_authorizer()
    processor = read_payment_processor()
    processor.pay(order, authorizer)

    print("Transaction complete")


if __name__ == "__main__":
    main()
