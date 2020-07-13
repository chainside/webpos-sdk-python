"""
Nigiri auto-generated file
"""
from sdkboil.object import SdkObject
from .payment_order_retrieval import PaymentOrderRetrieval
class PaymentOrderList(SdkObject):
    schema = {
  "rules": [],
  "schema": {
    "paymentorders": {
      "elements": {
        "rules": [],
        "schema": {
          "amount": {
            "rules": [
              "decimal",
              "required"
            ],
            "type": "string"
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
          "payment_data": {
            "rules": [
              "required",
              "nullable"
            ],
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
          "resolved_at": {
            "rules": [
              "required",
              "nullable"
            ],
            "type": "ISO_8601_date"
          },
          "status": {
            "rules": [
              "in:pending,paid,cancelled,expired,network_dispute,chargeback",
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
      "rules": [
        "required",
        "nullable"
      ],
      "type": "array"
    },
    "total_items": {
      "rules": [
        "required"
      ],
      "type": "integer"
    },
    "total_pages": {
      "rules": [
        "required"
      ],
      "type": "integer"
    }
  },
  "type": "object"
}
    sub_objects = {
                    'paymentorders': [PaymentOrderRetrieval],

        }
    def __init__(self, total_pages,total_items,paymentorders=None):
        super().__init__()
        self.paymentorders = paymentorders
        self.total_pages = total_pages
        self.total_items = total_items
