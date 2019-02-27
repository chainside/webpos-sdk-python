"""
Nigiri auto-generated file
"""
from sdkboil.object import SdkObject
from .payment_order_state import PaymentOrderState
from .transaction import Transaction
from .rate_retrieval import RateRetrieval
from .payment_order_creator import PaymentOrderCreator
from .currency_retrieval import CurrencyRetrieval


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
        'created_by': PaymentOrderCreator,
        'currency': CurrencyRetrieval,

    }

    def __init__(self, uuid, redirect_url, btc_amount, expires_in, created_at, amount, required_confirmations, state, uri, rate, created_by, expiration_time, currency, callback_url, address, transactions=None, reference=None, chargeback_date=None, details=None, dispute_start_date=None, resolved_at=None):
        super().__init__()
        self.uuid = uuid
        self.redirect_url = redirect_url
        self.btc_amount = btc_amount
        self.expires_in = expires_in
        self.created_at = created_at
        self.amount = amount
        self.required_confirmations = required_confirmations
        self.state = state
        self.transactions = transactions
        self.reference = reference
        self.chargeback_date = chargeback_date
        self.uri = uri
        self.rate = rate
        self.details = details
        self.created_by = created_by
        self.expiration_time = expiration_time
        self.currency = currency
        self.callback_url = callback_url
        self.address = address
        self.dispute_start_date = dispute_start_date
        self.resolved_at = resolved_at
