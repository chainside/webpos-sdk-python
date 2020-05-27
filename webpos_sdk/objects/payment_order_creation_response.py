"""
Nigiri auto-generated file
"""
from sdkboil.object import SdkObject
from .rate_retrieval import RateRetrieval
class PaymentOrderResponse(SdkObject):
    schema = {
  "rules": [],
  "schema": {
    "address": {
      "rules": [
        "regex:^(bc1|[13]|tb1|[2nm]|bcrt)[a-zA-HJ-NP-Z0-9]{25,40}$",
        "required"
      ],
      "type": "string"
    },
    "amount": {
      "rules": [
        "required"
      ],
      "type": "integer"
    },
    "created_at": {
      "rules": [
        "nullable"
      ],
      "type": "ISO_8601_date"
    },
    "expiration_time": {
      "rules": [
        "required"
      ],
      "type": "ISO_8601_date"
    },
    "expires_in": {
      "rules": [
        "required"
      ],
      "type": "integer"
    },
    "rate": {
      "rules": [
        "required"
      ],
      "schema": {
        "created_at": {
          "rules": [
            "required"
          ],
          "type": "ISO_8601_date"
        },
        "from": {
          "rules": [],
          "type": "string"
        },
        "source": {
          "rules": [
            "required"
          ],
          "type": "string"
        },
        "to": {
          "rules": [],
          "type": "string"
        },
        "value": {
          "rules": [
            "decimal",
            "required"
          ],
          "type": "string"
        }
      },
      "type": "object"
    },
    "redirect_url": {
      "rules": [
        "regex[https_url]:^https://",
        "required",
        "nullable"
      ],
      "type": "url"
    },
    "reference": {
      "rules": [
        "nullable"
      ],
      "type": "string"
    },
    "uri": {
      "rules": [
        "regex:^",
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
}
    sub_objects = {
                    'rate': RateRetrieval,

        }
    def __init__(self, expiration_time,expires_in,uuid,address,uri,rate,amount,redirect_url=None,created_at=None,reference=None):
        super().__init__()
        self.expiration_time = expiration_time
        self.expires_in = expires_in
        self.uuid = uuid
        self.address = address
        self.uri = uri
        self.redirect_url = redirect_url
        self.rate = rate
        self.amount = amount
        self.created_at = created_at
        self.reference = reference
