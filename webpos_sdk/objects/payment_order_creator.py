"""
Nigiri auto-generated file
"""
from sdkboil.object import SdkObject
from .deposit_account_lite import DepositAccountLite
class PaymentOrderCreator(SdkObject):
    schema = {
  "rules": [],
  "schema": {
    "active": {
      "rules": [],
      "type": "boolean"
    },
    "deposit_account": {
      "rules": [
        "required"
      ],
      "schema": {
        "name": {
          "rules": [
            "required"
          ],
          "type": "string"
        },
        "type": {
          "rules": [
            "in:bank,bitcoin",
            "required"
          ],
          "type": "string"
        },
        "uuid": {
          "rules": [
            "required"
          ],
          "type": "uuid"
        }
      },
      "type": "object"
    },
    "name": {
      "rules": [
        "required"
      ],
      "type": "string"
    },
    "type": {
      "rules": [
        "required",
        "in:web,mobile"
      ],
      "type": "string"
    },
    "uuid": {
      "rules": [
        "required"
      ],
      "type": "uuid"
    }
  },
  "type": "object"
}
    sub_objects = {
                    'deposit_account': DepositAccountLite,

        }
    def __init__(self, type,uuid,name,deposit_account,active=None):
        super().__init__()
        self.type = type
        self.active = active
        self.uuid = uuid
        self.name = name
        self.deposit_account = deposit_account
