from dataclasses import dataclass

PAYOUT_HOLIDAY_DAYS = 5


@dataclass
class Employee:
    """Basic representation of an employee at the company."""

    name: str
    role: str
    vacation_days: int = 25

    def payout_holiday(self) -> None:
        """Pay out a holiday."""
        if self.vacation_days < PAYOUT_HOLIDAY_DAYS:
            raise ValueError(
                f"You don't have enough holidays left over for a payout.\
                Remaining holidays: {self.vacation_days}."
            )
        self.vacation_days -= PAYOUT_HOLIDAY_DAYS
        print(f"Paying out a holiday. Holidays left: {self.vacation_days}")

    def take_a_single_holiday(self) -> None:
        # check whether the employee still has holidays left
        if self.vacation_days < 1:
            raise ValueError("You don't have any holidays left. Now back to work, you!")
        self.vacation_days -= 1
        print("Have fun on your holiday. Don't forget to check your emails!")
