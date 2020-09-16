"""
Nigiri auto-generated file
"""
from .common import ChainsideAction, ChainsideAuthenticatedAction, ChainsideAuthenticatingAction
from ..objects import *
from ..exceptions import *





class GetPaymentOrdersAction(ChainsideAuthenticatedAction):
    route = '/payment-order'
    verb = 'GET'
    headers = {}
    query_parameters_schema = {'status': {'type': 'string', 'rules': ['in:pending,partial,mempool_unconfirmed,unconfirmed,paid,cancelled,expired,network_dispute,mempool_network_dispute,possible_chargeback,chargeback'], 'description': 'Status of the payment orders to retrieve'}, 'sort_by': {'type': 'string', 'rules': ['in:amount,created_at', 'nullable'], 'description': 'Field used to sort pages (default: created_at)'}, 'sort_order': {'type': 'string', 'rules': ['in:asc,desc', 'nullable'], 'description': 'Ordering to be used for the sort (default: desc)'}, 'page': {'type': 'integer', 'rules': ['nullable', 'min:0'], 'description': 'Index of the page to be returned (default: 0)'}, 'page_size': {'type': 'integer', 'rules': ['nullable', 'max:40'], 'description': 'Size of the returned page (default: 20)'}}
    route_parameters_schema = {}
    request_body_class = None
    response_body_class = PaymentOrderList
    errors = dict(super(ChainsideAuthenticatedAction, ChainsideAuthenticatedAction).errors, **{
        '1012':ForbiddenException,
})



    @property
    def status(self):
        return self.query_parameters['status']
    @status.setter
    def status(self, value):
        self.query_parameters['status'] = value

    @property
    def sort_by(self):
        return self.query_parameters['sort_by']
    @sort_by.setter
    def sort_by(self, value):
        self.query_parameters['sort_by'] = value

    @property
    def sort_order(self):
        return self.query_parameters['sort_order']
    @sort_order.setter
    def sort_order(self, value):
        self.query_parameters['sort_order'] = value

    @property
    def page(self):
        return self.query_parameters['page']
    @page.setter
    def page(self, value):
        self.query_parameters['page'] = value

    @property
    def page_size(self):
        return self.query_parameters['page_size']
    @page_size.setter
    def page_size(self, value):
        self.query_parameters['page_size'] = value


