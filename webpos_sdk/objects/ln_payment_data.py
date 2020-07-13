"""
Nigiri auto-generated file
"""
from sdkboil.object import SdkObject
class LnPaymentData(SdkObject):
    schema = {
  "rules": [],
  "schema": {
    "invoice": {
      "rules": [
        "required"
      ],
      "type": "string"
    }
  },
  "type": "object"
}
    sub_objects = {
            
        }
    def __init__(self, invoice):
        super().__init__()
        self.invoice = invoice
