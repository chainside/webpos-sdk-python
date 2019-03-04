"""
Nigiri auto-generated file
"""
from sdkboil.exception import SdkHttpException


class UnauthorizedClientException(SdkHttpException):
    error_code = '1001'


class InvalidRealmException(SdkHttpException):
    error_code = '1018'


class TooManyRequestsException(SdkHttpException):
    error_code = '2000'


class ValidationErrorException(SdkHttpException):
    error_code = '0001'


class AccessTokenExpiredException(SdkHttpException):
    error_code = '1004'


class InvalidScopeException(SdkHttpException):
    error_code = '1013'


class InvalidGrantTypeException(SdkHttpException):
    error_code = '1002'


class ForbiddenException(SdkHttpException):
    error_code = '1012'


class InvalidAccessTokenException(SdkHttpException):
    error_code = '1007'


class InvalidAuthorizationHeaderException(SdkHttpException):
    error_code = '3007'


class InvalidRefreshTokenException(SdkHttpException):
    error_code = '1006'


class FunctionalityDownException(SdkHttpException):
    error_code = '4006'


class InternalServerErrorException(SdkHttpException):
    error_code = '4000'


class MethodNotAllowedException(SdkHttpException):
    error_code = '3003'


class InvalidAcceptHeaderException(SdkHttpException):
    error_code = '3013'


class RateUnavailableException(SdkHttpException):
    error_code = '4003'


class NotFoundException(SdkHttpException):
    error_code = '3001'


class InvalidContentTypeHeaderException(SdkHttpException):
    error_code = '3012'


class InvalidCallbackException(SdkHttpException):
    error_code = '0013'
