"""
Nigiri auto-generated file
"""
from sdkboil.object import SdkObject
class PaymentOrder(SdkObject):
    schema = {
  "rules": [],
  "schema": {
    "amount": {
      "rules": [
        "required",
        "decimal"
      ],
      "type": "string"
    },
    "callback_url": {
      "rules": [
        "regex[https_url]:^https://",
        "nullable",
        "maxlen:300"
      ],
      "type": "url"
    },
    "cancel_url": {
      "rules": [
        "regex[https_url]:^https://",
        "nullable",
        "maxlen:300"
      ],
      "type": "url"
    },
    "continue_url": {
      "rules": [
        "regex[https_url]:^https://",
        "nullable",
        "maxlen:300"
      ],
      "type": "url"
    },
    "details": {
      "rules": [
        "maxlen:300",
        "nullable"
      ],
      "type": "string"
    },
    "reference": {
      "rules": [
        "maxlen:300",
        "nullable"
      ],
      "type": "string"
    },
    "required_confirmations": {
      "rules": [
        "min:0",
        "nullable"
      ],
      "type": "integer"
    }
  },
  "type": "object"
}
    sub_objects = {
            
        }
    def __init__(self, amount,cancel_url=None,continue_url=None,callback_url=None,details=None,reference=None,required_confirmations=None):
        super().__init__()
        self.amount = amount
        self.cancel_url = cancel_url
        self.continue_url = continue_url
        self.callback_url = callback_url
        self.details = details
        self.reference = reference
        self.required_confirmations = required_confirmations
