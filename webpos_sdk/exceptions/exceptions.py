"""
Nigiri auto-generated file
"""
from sdkboil.exception import SdkHttpException


class MethodNotAllowedException(SdkHttpException):
    error_code = '3003'


class InvalidRefreshTokenException(SdkHttpException):
    error_code = '1006'


class InvalidAcceptHeaderException(SdkHttpException):
    error_code = '3013'


class NotFoundException(SdkHttpException):
    error_code = '3001'


class InvalidGrantTypeException(SdkHttpException):
    error_code = '1002'


class TooManyRequestsException(SdkHttpException):
    error_code = '2000'


class ValidationErrorException(SdkHttpException):
    error_code = '0001'


class InvalidAccessTokenException(SdkHttpException):
    error_code = '1007'


class InvalidAuthorizationHeaderException(SdkHttpException):
    error_code = '3007'


class InvalidScopeException(SdkHttpException):
    error_code = '1013'


class InternalServerErrorException(SdkHttpException):
    error_code = '4000'


class UnauthorizedClientException(SdkHttpException):
    error_code = '1001'


class ForbiddenException(SdkHttpException):
    error_code = '1012'


class InvalidRealmException(SdkHttpException):
    error_code = '1018'


class InvalidCallbackException(SdkHttpException):
    error_code = '0013'


class InvalidContentTypeHeaderException(SdkHttpException):
    error_code = '3012'


class AccessTokenExpiredException(SdkHttpException):
    error_code = '1004'
