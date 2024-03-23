from enum import Enum, auto


class PaymentStatus(Enum):
    OPEN = auto()
    PAID = auto()
