"""
Nigiri auto-generated file
"""
from sdkboil.object import SdkObject
from .payment_order_state import PaymentOrderState
from .transaction import Transaction
from .rate_retrieval import RateRetrieval
from .currency_retrieval import CurrencyRetrieval
from .payment_order_creator import PaymentOrderCreator
class PaymentOrderRetrieval(SdkObject):
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
        "regex[https_url]:^https://"
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
        "regex[https_url]:^https://"
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
            "nullable",
            "required"
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
            "nullable",
            "required"
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
            "nullable",
            "required"
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
                    'state': PaymentOrderState,
        'transactions': [Transaction],
        'rate': RateRetrieval,
        'currency': CurrencyRetrieval,
        'created_by': PaymentOrderCreator,

        }
    def __init__(self, expiration_time,expires_in,btc_amount,state,currency,amount,created_by,required_confirmations,uuid,address,uri,rate,created_at,resolved_at=None,transactions=None,details=None,callback_url=None,redirect_url=None,dispute_start_date=None,chargeback_date=None,reference=None):
        super().__init__()
        self.expiration_time = expiration_time
        self.expires_in = expires_in
        self.btc_amount = btc_amount
        self.resolved_at = resolved_at
        self.state = state
        self.currency = currency
        self.amount = amount
        self.created_by = created_by
        self.required_confirmations = required_confirmations
        self.transactions = transactions
        self.details = details
        self.uuid = uuid
        self.address = address
        self.uri = uri
        self.callback_url = callback_url
        self.redirect_url = redirect_url
        self.dispute_start_date = dispute_start_date
        self.rate = rate
        self.chargeback_date = chargeback_date
        self.created_at = created_at
        self.reference = reference
