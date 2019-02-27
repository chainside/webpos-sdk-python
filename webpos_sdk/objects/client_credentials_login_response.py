"""
Nigiri auto-generated file
"""
from sdkboil.object import SdkObject


class ClientCredentialsLoginResponse(SdkObject):
    schema = {
        "rules": [],
        "schema": {
            "access_token": {
                "rules": [
                    "required"
                ],
                "type": "string"
            },
            "expires_in": {
                "rules": [
                    "required"
                ],
                "type": "integer"
            },
            "id_token": {
                "rules": [
                    "regex:^[A-Za-z0-9-_=]+\\.[A-Za-z0-9-_=]+\\.?[A-Za-z0-9-_.+/=]*$",
                    "required"
                ],
                "type": "string"
            },
            "scope": {
                "rules": [
                    "nullable"
                ],
                "type": "string"
            },
            "token_type": {
                "rules": [
                    "equals:Bearer",
                    "required"
                ],
                "type": "string"
            }
        },
        "type": "object"
    }
    sub_objects = {

    }

    def __init__(self, access_token, id_token, token_type, expires_in, scope=None):
        super().__init__()
        self.access_token = access_token
        self.id_token = id_token
        self.token_type = token_type
        self.expires_in = expires_in
        self.scope = scope
