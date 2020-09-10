"""
Nigiri auto-generated file
"""
from sdkboil.object import SdkObject
from .paid_status import PaidStatus
from .paid_status import PaidStatus
from .paid_status import PaidStatus
class PaymentOrderState(SdkObject):
    schema = {
  "rules": [],
  "schema": {
    "blockchain_status": {
      "rules": [
        "in:pending,partial,mempool_unconfirmed,unconfirmed,paid,cancelled,expired,network_dispute,mempool_network_dispute,possible_chargeback,chargeback",
        "required"
      ],
      "type": "string"
    },
    "in_confirmation": {
      "rules": [
        "required",
        "nullable"
      ],
      "schema": {
        "crypto": {
          "rules": [
            "required"
          ],
          "type": "integer"
        },
        "fiat": {
          "rules": [
            "required",
            "decimal"
          ],
          "type": "string"
        }
      },
      "type": "object"
    },
    "paid": {
      "rules": [
        "required",
        "nullable"
      ],
      "schema": {
        "crypto": {
          "rules": [
            "required"
          ],
          "type": "integer"
        },
        "fiat": {
          "rules": [
            "required",
            "decimal"
          ],
          "type": "string"
        }
      },
      "type": "object"
    },
    "unpaid": {
      "rules": [
        "required",
        "nullable"
      ],
      "schema": {
        "crypto": {
          "rules": [
            "required"
          ],
          "type": "integer"
        },
        "fiat": {
          "rules": [
            "required",
            "decimal"
          ],
          "type": "string"
        }
      },
      "type": "object"
    }
  },
  "type": "object"
}
    sub_objects = {
                    'in_confirmation': PaidStatus,
        'paid': PaidStatus,
        'unpaid': PaidStatus,

        }
    def __init__(self, blockchain_status,in_confirmation=None,paid=None,unpaid=None):
        super().__init__()
        self.in_confirmation = in_confirmation
        self.paid = paid
        self.blockchain_status = blockchain_status
        self.unpaid = unpaid
