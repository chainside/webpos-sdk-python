"""
Nigiri auto-generated file
"""
from sdkboil.object import SdkObject
class PaymentOrderResponse(SdkObject):
    schema = {
  "rules": [],
  "schema": {
    "created_at": {
      "rules": [
        "nullable"
      ],
      "type": "ISO_8601_date"
    },
    "redirect_url": {
      "rules": [
        "regex[https_url]:^https://",
        "required",
        "nullable"
      ],
      "type": "url"
    },
    "reference": {
      "rules": [
        "nullable"
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
    def __init__(self, uuid,redirect_url=None,reference=None,created_at=None):
        super().__init__()
        self.redirect_url = redirect_url
        self.uuid = uuid
        self.reference = reference
        self.created_at = created_at
