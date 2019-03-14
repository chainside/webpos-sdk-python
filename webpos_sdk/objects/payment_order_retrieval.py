"""
Nigiri auto-generated file
"""
from sdkboil.object import SdkObject
from .transaction import Transaction
from .currency_retrieval import CurrencyRetrieval
from .payment_order_creator import PaymentOrderCreator
from .payment_order_state import PaymentOrderState
from .rate_retrieval import RateRetrieval
class PaymentOrderRetrieval(SdkObject):
    schema = {
  "rules": [],
  "schema": {
    "address": {
      "rules": [
        "required"
      ],
      "type": "base58"
    },
    "amount": {
      "rules": [
        "decimal",
        "required"
      ],
      "type": "string"
    },
    "btc_amount": {
      "rules": [
        "required"
      ],
      "type": "integer"
    },
    "callback_url": {
      "rules": [
        "regex[https_url]:^https://",
        "required"
      ],
      "type": "url"
    },
    "chargeback_date": {
      "rules": [
        "required",
        "nullable"
      ],
      "type": "ISO_8601_date"
    },
    "created_at": {
      "rules": [
        "required"
      ],
      "type": "ISO_8601_date"
    },
    "created_by": {
      "rules": [
        "required"
      ],
      "schema": {
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
            "in:web"
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
    "currency": {
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
            "in:crypto,fiat",
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
    "details": {
      "rules": [
        "required",
        "nullable"
      ],
      "type": "string"
    },
    "dispute_start_date": {
      "rules": [
        "required",
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
        "source": {
          "rules": [
            "required"
          ],
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
        "required"
      ],
      "type": "url"
    },
    "reference": {
      "rules": [
        "nullable",
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
    "resolved_at": {
      "rules": [
        "required",
        "nullable"
      ],
      "type": "ISO_8601_date"
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
        "status": {
          "rules": [
            "in:pending,paid,cancelled,expired,network_dispute,chargeback",
            "required"
          ],
          "type": "string"
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
        "nullable",
        "required"
      ],
      "type": "array"
    },
    "uri": {
      "rules": [
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
                    'transactions': [Transaction],
        'currency': CurrencyRetrieval,
        'created_by': PaymentOrderCreator,
        'state': PaymentOrderState,
        'rate': RateRetrieval,

        }
    def __init__(self, required_confirmations,currency,btc_amount,amount,created_at,created_by,state,redirect_url,uuid,callback_url,expiration_time,uri,rate,address,expires_in,transactions=None,reference=None,chargeback_date=None,details=None,resolved_at=None,dispute_start_date=None):
        super().__init__()
        self.transactions = transactions
        self.required_confirmations = required_confirmations
        self.currency = currency
        self.btc_amount = btc_amount
        self.amount = amount
        self.created_at = created_at
        self.reference = reference
        self.created_by = created_by
        self.chargeback_date = chargeback_date
        self.details = details
        self.state = state
        self.redirect_url = redirect_url
        self.uuid = uuid
        self.callback_url = callback_url
        self.resolved_at = resolved_at
        self.expiration_time = expiration_time
        self.uri = uri
        self.rate = rate
        self.address = address
        self.expires_in = expires_in
        self.dispute_start_date = dispute_start_date
