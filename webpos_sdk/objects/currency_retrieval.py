"""
Nigiri auto-generated file
"""
from sdkboil.object import SdkObject


class CurrencyRetrieval(SdkObject):
    schema = {
        "rules": [],
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
    }
    sub_objects = {

    }

    def __init__(self, uuid, type, name):
        super().__init__()
        self.uuid = uuid
        self.type = type
        self.name = name
