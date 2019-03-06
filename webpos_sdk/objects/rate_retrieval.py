"""
Nigiri auto-generated file
"""
from sdkboil.object import SdkObject


class RateRetrieval(SdkObject):
    schema = {
        "rules": [],
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
    }
    sub_objects = {

    }

    def __init__(self, created_at, source, value):
        super().__init__()
        self.created_at = created_at
        self.source = source
        self.value = value
