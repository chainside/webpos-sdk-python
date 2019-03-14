"""
Nigiri auto-generated file
"""
from . import *
from sdkboil.actions import ActionsFactory

class ChainsideFactory(ActionsFactory):
    actions = {
        'client_credentials_login' : ClientCredentialsLoginAction,
        'get_callbacks' : GetCallbacksAction,
        'payment_reset' : PaymentResetAction,
        'payment_update' : PaymentUpdateAction,
        'delete_payment_order' : DeletePaymentOrderAction,
        'get_payment_order' : GetPaymentOrderAction,
        'get_web_pos_payments' : GetWebPosPaymentsAction,
        'create_payment_order' : CreatePaymentOrderAction,
}