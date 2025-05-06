from dataclasses import dataclass


@dataclass
class Employee:
    """Basic representation of an employee at the company."""

    name: str
    role: str
    vacation_days: int = 25

    def take_a_holiday(self, payout: bool) -> None:
        """Let the employee take a single holiday, or pay out 5 holidays."""
        if payout:
            # check whether self.vacation_days is less than 5
            if self.vacation_days < 5:
                raise ValueError(
                    f"You don't have enough holidays left over for a payout.\
                    Remaining holidays: {self.vacation_days}."
                )
            self.vacation_days -= 5
            print(f"Pyaing out a holiday. Holidays left: {self.vacation_days}")
        else:
            # check whether self.vacation_days is less than 1
            if self.vacation_days < 1:
                raise ValueError(
                    "You don't have any holidays left. Now back to work, you!"
                )
            self.vacation_days -= 1
            print("Have fun on your holiday. Don't forget to check your emails!")


@dataclass
class HourlyEmployee(Employee):
    hourly_rate: float = 50
    amount: int = 10


@dataclass
class SalariedEmployee(Employee):
    monthly_salary: float = 50000


@dataclass
class Freelancer(Employee):
    hourly_rate: float = 50
    amount: int = 10
    retainer: float = 1000


@dataclass
class Intern(Employee):
    monthly_salary: float = 1000
