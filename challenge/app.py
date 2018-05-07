from bottle import Bottle, HTTPResponse

app = Bottle()


@app.get('/api/v1/health')
def health():
    return HTTPResponse(status=200, body="Healthy")

