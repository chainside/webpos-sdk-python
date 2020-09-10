"""
Nigiri auto-generated file
"""
from sdkboil.object import SdkObject
from .rate_retrieval import RateRetrieval
from .bitcoin_payment_data import BitcoinPaymentData
from .ln_payment_data import LnPaymentData
class PaymentData(SdkObject):
    schema = {
  "rules": [],
  "schema": {
    "amount": {
      "rules": [
        "required",
        "nullable"
      ],
      "type": "integer"
    },
    "bitcoin": {
      "rules": [
        "nullable"
      ],
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
    },
    "expiration_time": {
      "rules": [
        "required"
      ],
      "type": "ISO_8601_date"
    },
    "expires_in": {
      "rules": [
        "required",
        "nullable"
      ],
      "type": "integer"
    },
    "ln": {
      "rules": [
        "nullable"
      ],
      "schema": {
        "invoice": {
          "rules": [
            "required"
          ],
          "type": "string"
        }
      },
      "type": "object"
    },
    "payment_method": {
      "rules": [
        "required",
        "nullable"
      ],
      "type": "string"
    },
    "rate": {
      "rules": [
        "required",
        "nullable"
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
    }
  },
  "type": "object"
}
    sub_objects = {
                    'rate': RateRetrieval,
        'bitcoin': BitcoinPaymentData,
        'ln': LnPaymentData,

        }
    def __init__(self, expiration_time,payment_method=None,amount=None,rate=None,expires_in=None,bitcoin=None,ln=None):
        super().__init__()
        self.payment_method = payment_method
        self.expiration_time = expiration_time
        self.amount = amount
        self.rate = rate
        self.expires_in = expires_in
        self.bitcoin = bitcoin
        self.ln = ln
