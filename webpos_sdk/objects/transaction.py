"""
Nigiri auto-generated file
"""
from sdkboil.object import SdkObject
from .out import Out
class Transaction(SdkObject):
    schema = {
  "rules": [],
  "schema": {
    "blockchain_status": {
      "rules": [
        "required",
        "in:mempool,unconfirmed,confirmed,reverted"
      ],
      "type": "string"
    },
    "created_at": {
      "rules": [
        "required"
      ],
      "type": "ISO_8601_date"
    },
    "normalized_txid": {
      "rules": [
        "len:64",
        "required"
      ],
      "type": "string"
    },
    "outs": {
      "elements": {
        "rules": [],
        "schema": {
          "amount": {
            "rules": [
              "required"
            ],
            "type": "integer"
          },
          "n": {
            "rules": [
              "required"
            ],
            "type": "integer"
          }
        },
        "type": "object"
      },
      "rules": [
        "required"
      ],
      "type": "array"
    },
    "outs_sum": {
      "rules": [
        "required"
      ],
      "type": "integer"
    },
    "status": {
      "rules": [
        "required",
        "in:unconfirmed,confirmed,reverted"
      ],
      "type": "string"
    },
    "txid": {
      "rules": [
        "len:64",
        "required"
      ],
      "type": "string"
    }
  },
  "type": "object"
}
    sub_objects = {
                    'outs': [Out],

        }
    def __init__(self, txid,normalized_txid,blockchain_status,outs_sum,status,created_at,outs):
        super().__init__()
        self.txid = txid
        self.normalized_txid = normalized_txid
        self.blockchain_status = blockchain_status
        self.outs_sum = outs_sum
        self.status = status
        self.created_at = created_at
        self.outs = outs
