"""
Nigiri auto-generated file
"""
from sdkboil.object import SdkObject
from .paid_status import PaidStatus
from .paid_status import PaidStatus
from .paid_status import PaidStatus


class PaymentOrderState(SdkObject):
    schema = {
        "rules": [],
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
    }
    sub_objects = {
        'paid': PaidStatus,
        'in_confirmation': PaidStatus,
        'unpaid': PaidStatus,

    }

    def __init__(self, status, blockchain_status, paid=None, in_confirmation=None, unpaid=None):
        super().__init__()
        self.paid = paid
        self.in_confirmation = in_confirmation
        self.unpaid = unpaid
        self.status = status
        self.blockchain_status = blockchain_status
