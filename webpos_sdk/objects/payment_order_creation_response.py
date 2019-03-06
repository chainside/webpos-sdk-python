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
                    "regex:^",
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
                    "required",
                    "nullable"
                ],
                "type": "url"
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

    def __init__(self, expiration_time, expires_in, uri, rate, uuid, amount, address, redirect_url=None):
        super().__init__()
        self.expiration_time = expiration_time
        self.expires_in = expires_in
        self.uri = uri
        self.rate = rate
        self.uuid = uuid
        self.amount = amount
        self.redirect_url = redirect_url
        self.address = address
