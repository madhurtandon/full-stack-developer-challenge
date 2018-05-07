import json
from bottle import Bottle, HTTPResponse, request, response
from config import MDB_CONFIG
from challenge.db.story import Story
from challenge.validations.field_required import is_required, is_status_valid

app = Bottle()


@app.route("/api/v1/health.json", method="GET")
def health():
    return HTTPResponse(status=200, body="Healthy")


@app.route("/api/v1/stories.json", method="POST")
@is_required
@is_status_valid
def story():
    data = request.forms
    title = data.title
    description = data.description
    status = data.status
    author_id = data.author_id

    db = Story(**MDB_CONFIG)
    with db as cursor:
        db.create_story(cursor, title, description, db.get_status(status), author_id)

    payload = {"title": title,
               "description": description,
               "status": status,
               "author_id": author_id}

    return HTTPResponse(status=201, body=payload)

