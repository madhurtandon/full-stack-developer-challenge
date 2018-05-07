"""
Utitlitis for validations.
"""

from functools import wraps
from bottle import HTTPResponse


def validation_decorator(f, validation=lambda: False, response=HTTPResponse(403)):
    """
    Given a function, a validation rule and a response creates a decorator
    that will perform that validaion and return the passed response on
    success otherwise calls the function.

    Args:
        f (func): python object that implements __call__.
        validation (func): function that returns a boolean.
        response (bottle.Response): Response object.

    Returns:
        @func: a decorator
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        if validation():
            return response

        return f(*args, **kwargs)
    return decorated
