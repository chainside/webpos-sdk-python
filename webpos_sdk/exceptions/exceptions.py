"""
Nigiri auto-generated file
"""
from sdkboil.exception import SdkHttpException


class InvalidScopeException(SdkHttpException):
    error_code = '1013'


class RateUnavailableException(SdkHttpException):
    error_code = '4003'


class MethodNotAllowedException(SdkHttpException):
    error_code = '3003'


class InvalidCallbackException(SdkHttpException):
    error_code = '0013'


class UnauthorizedClientException(SdkHttpException):
    error_code = '1001'


class FunctionalityDownException(SdkHttpException):
    error_code = '4006'


class ForbiddenException(SdkHttpException):
    error_code = '1012'


class InvalidGrantTypeException(SdkHttpException):
    error_code = '1002'


class InvalidContentTypeHeaderException(SdkHttpException):
    error_code = '3012'


class InternalServerErrorException(SdkHttpException):
    error_code = '4000'


class InvalidRefreshTokenException(SdkHttpException):
    error_code = '1006'


class AccessTokenExpiredException(SdkHttpException):
    error_code = '1004'


class InvalidRealmException(SdkHttpException):
    error_code = '1018'


class ValidationErrorException(SdkHttpException):
    error_code = '0001'


class TooManyRequestsException(SdkHttpException):
    error_code = '2000'


class InvalidAccessTokenException(SdkHttpException):
    error_code = '1007'


class InvalidAcceptHeaderException(SdkHttpException):
    error_code = '3013'


class InvalidAuthorizationHeaderException(SdkHttpException):
    error_code = '3007'


class NotFoundException(SdkHttpException):
    error_code = '3001'
