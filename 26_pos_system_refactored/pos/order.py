from dataclasses import dataclass, field
from pos.data import PaymentStatus


@dataclass
class LineItem:
    item: str
    quantity: int
    price: int

    @property
    def total_price(self) -> int:
        return self.quantity * self.price


@dataclass
class Order:
    items: list[LineItem] = field(default_factory=list)
    status: PaymentStatus = PaymentStatus.OPEN

    def add_item(self, item: LineItem) -> None:
        self.items.append(item)

    def set_payment_status(self, status: PaymentStatus) -> None:
        self.status = status

    @property
    def total_price(self) -> int:
        return sum(item.total_price for item in self.items)
