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

    def __init__(self, expires_in, address, uri, uuid, amount, expiration_time, rate, redirect_url=None):
        super().__init__()
        self.expires_in = expires_in
        self.address = address
        self.uri = uri
        self.uuid = uuid
        self.amount = amount
        self.expiration_time = expiration_time
        self.redirect_url = redirect_url
        self.rate = rate
