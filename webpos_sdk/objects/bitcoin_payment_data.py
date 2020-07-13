"""
Nigiri auto-generated file
"""
from sdkboil.object import SdkObject
from .transaction import Transaction
from .payment_order_state import PaymentOrderState
class BitcoinPaymentData(SdkObject):
    schema = {
  "rules": [],
  "schema": {
    "address": {
      "rules": [
        "required"
      ],
      "type": "string"
    },
    "required_confirmations": {
      "rules": [
        "required"
      ],
      "type": "integer"
    },
    "state": {
      "rules": [
        "required"
      ],
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
    },
    "transactions": {
      "elements": {
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
      },
      "rules": [
        "required",
        "nullable"
      ],
      "type": "array"
    },
    "uri": {
      "rules": [
        "required"
      ],
      "type": "string"
    }
  },
  "type": "object"
}
    sub_objects = {
                    'transactions': [Transaction],
        'state': PaymentOrderState,

        }
    def __init__(self, uri,address,required_confirmations,state,transactions=None):
        super().__init__()
        self.uri = uri
        self.transactions = transactions
        self.address = address
        self.required_confirmations = required_confirmations
        self.state = state
