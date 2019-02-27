"""
Nigiri auto-generated file
"""
from sdkboil.object import SdkObject


class PaymentOrder(SdkObject):
    schema = {
        "rules": [],
        "schema": {
            "amount": {
                "rules": [
                    "required",
                    "decimal"
                ],
                "type": "string"
            },
            "callback_url": {
                "rules": [
                    "regex[https_url]:^https://",
                    "nullable"
                ],
                "type": "url"
            },
            "cancel_url": {
                "rules": [
                    "regex[https_url]:^https://",
                    "nullable"
                ],
                "type": "url"
            },
            "continue_url": {
                "rules": [
                    "regex[https_url]:^https://",
                    "nullable"
                ],
                "type": "url"
            },
            "details": {
                "rules": [
                    "required"
                ],
                "type": "string"
            },
            "reference": {
                "rules": [],
                "type": "string"
            },
            "required_confirmations": {
                "rules": [
                    "min:0",
                    "required"
                ],
                "type": "integer"
            }
        },
        "type": "object"
    }
    sub_objects = {

    }

    def __init__(self, amount, required_confirmations, details, callback_url=None, continue_url=None, reference=None, cancel_url=None):
        super().__init__()
        self.callback_url = callback_url
        self.amount = amount
        self.required_confirmations = required_confirmations
        self.continue_url = continue_url
        self.reference = reference
        self.details = details
        self.cancel_url = cancel_url
