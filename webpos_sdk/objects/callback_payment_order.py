"""
Nigiri auto-generated file
"""
from sdkboil.object import SdkObject
class CallbackPaymentOrder(SdkObject):
    schema = {
  "rules": [],
  "schema": {
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
    def __init__(self, uuid):
        super().__init__()
        self.uuid = uuid
