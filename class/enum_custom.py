from enum import Enum
from functools import total_ordering


@total_ordering
class PaymentStatus(Enum):
    PENDING = 1
    COMPLETED = 2
    REFUNDED = 3

    def __str__(self):
        return f'{self.name.lower()}({self.value})'

    def __eq__(self, other):
        if isinstance(other, int):
            return self.value == other

        if isinstance(other, PaymentStatus):
            return self is other

        return False

    def __lt__(self, other):
        if isinstance(other, int):
            return self.value < other

        if isinstance(other, PaymentStatus):
            return self.value < other.value

        return False

    def __bool__(self):
        if self is self.COMPLETED:
            return True

        return False


for member in PaymentStatus:
    print(member, bool(member))