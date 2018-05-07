from bottle import HTTPResponse, request
from challenge.db.story import Story
from challenge.validations.utils import validation_decorator


def is_required(f):
    required = HTTPResponse("Required fields are missing", status=400)

    def required_fields():
        data = request.forms
        title = data.get('title', None)
        description = data.get('description', None)
        status = data.get('status', None)
        if title is None or description is None or status is None:
            return True

    return validation_decorator(f, validation=required_fields, response=required)


def is_status_valid(f):
    is_valid = HTTPResponse("Invalid status", status=400)

    def status():
        data = request.forms
        status = str(data.get('status'))
        status = status.lower()

        # Convert status value from human readable format
        if status == 'published':
            return False
        elif status == 'draft':
            return False
        else:
            return True

    return validation_decorator(f, validation=status, response=is_valid)
