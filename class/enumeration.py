from enum import Enum
import json

class ResponseStatus(Enum):
    PENDING = 'pending'
    FULFILLED = 'fulfilled'
    REJECTED = 'rejected'

response = '''{
    "status":"fulfilled"
}'''

# print(response)
data = json.loads(response)
# print(data)
status = data['status']

try:
    if ResponseStatus(status) is ResponseStatus.FULFILLED:
        print('The request completed successfully')
except ValueError as error:
    print(error)

# customized enum class
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


if PaymentStatus.PENDING == PaymentStatus.PENDING:
    print('The payment is pending.')

if PaymentStatus.PENDING == 1:
    print('The payment is pending.')