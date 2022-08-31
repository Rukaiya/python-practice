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