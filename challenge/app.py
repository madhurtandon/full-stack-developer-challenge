import json
from bottle import Bottle, HTTPResponse, request, response
from config import MDB_CONFIG
from challenge.db.story import Story
from challenge.validations.field_required import is_required, is_status_valid

app = Bottle()


def enable_cors(fn):
    def _enable_cors(*args, **kwargs):
        # set CORS headers
        response.headers['Access-Control-Allow-Origin'] = 'http://localhost:3000'
        response.headers['Access-Control-Allow-Methods'] = 'POST, PUT, DELETE, GET, OPTIONS'
        response.headers['Access-Control-Allow-Headers'] = 'X-Requested-With, Content-Type'
        response.headers['Access-Control-Allow-Credentials'] = 'true'

        if request.method != 'OPTIONS':
            # actual request; reply with the actual response
            return fn(*args, **kwargs)

    return _enable_cors


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


@app.route("/api/v1/stories.json", method=['OPTIONS', 'GET'])
@enable_cors
def story():
    if request.method == 'OPTIONS':
        return {}
    else:
        db = Story(**MDB_CONFIG)
        with db as cursor:
            results = db.get_stories(cursor)

        stories = {"status": 200, "data": []}
        for result in results:
            db_result = {'story_id': result['story_id'],
                         'title': result['title'],
                         'description': result['description'],
                         'status': 'PUBLISHED' if result['status'] == Story.STATUS_PUBLISHED else 'DRAFT',
                         'author_id': result['author_id']}

            stories['data'].append(db_result)

        stories = json.dumps(stories)
        return HTTPResponse(status=200, body=stories)
