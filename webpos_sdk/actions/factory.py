"""
Nigiri auto-generated file
"""
from . import *
from sdkboil.actions import ActionsFactory

class ChainsideFactory(ActionsFactory):
    actions = {
        'delete_payment_order' : DeletePaymentOrderAction,
        'get_payment_order' : GetPaymentOrderAction,
        'get_payment_orders' : GetPaymentOrdersAction,
        'create_payment_order' : CreatePaymentOrderAction,
        'client_credentials_login' : ClientCredentialsLoginAction,
        'get_callbacks' : GetCallbacksAction,
        'payment_reset' : PaymentResetAction,
        'payment_update' : PaymentUpdateAction,
}