from enum import IntEnum
from http import HTTPStatus


class ErrorCode(IntEnum):
    BAD_REQUEST = HTTPStatus.BAD_REQUEST
    UNAUTHENTICATED = HTTPStatus.UNAUTHORIZED
    UNAUTHORIZED = HTTPStatus.FORBIDDEN
    VALIDATION_ERROR = HTTPStatus.UNPROCESSABLE_ENTITY
    UNHANDLED_SERVER_ERROR = HTTPStatus.INTERNAL_SERVER_ERROR

    USER_NOT_FOUND = 40001
    USER_ALREADY_EXISTS = 40002
    FIRST_SUPER_USER_DELETE_FORBIDDEN = 40003

    MOVIE_NOT_FOUND = 50001
    MOVIE_ALREADY_EXISTS = 50002

    REVIEW_NOT_FOUND = 60001
    REVIEW_ALREADY_EXISTS = 60002