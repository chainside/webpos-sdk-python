"""
Nigiri auto-generated file
"""
from sdkboil.object import SdkObject

from .callback_payment_order import CallbackPaymentOrder
class PaymentDisputeStartCallback(SdkObject):
    schema = {
  "rules": [
    "nullable"
  ],
  "schema": {
    "created_at": {
      "rules": [
        "required"
      ],
      "type": "ISO_8601_date"
    },
    "event": {
      "rules": [
        "required",
        "equals:payment.dispute.start"
      ],
      "type": "string"
    },
    "object": {
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
    },
    "object_type": {
      "rules": [
        "required",
        "nullable"
      ],
      "type": "string"
    }
  },
  "type": "object"
}
    sub_objects = {
            'object': CallbackPaymentOrder
        }
    def __init__(self, event,created_at,object_type=None,object=None):
        super().__init__()
        self.event = event
        self.created_at = created_at
        self.object_type = object_type
        self.object = object
