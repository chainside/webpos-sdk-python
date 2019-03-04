"""
Nigiri auto-generated file
"""
from sdkboil.object import SdkObject
from .deposit_account_lite import DepositAccountLite


class PaymentOrderCreator(SdkObject):
    schema = {
        "rules": [],
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
    }
    sub_objects = {
        'deposit_account': DepositAccountLite,

    }

    def __init__(self, uuid, deposit_account, type, name):
        super().__init__()
        self.uuid = uuid
        self.deposit_account = deposit_account
        self.type = type
        self.name = name
