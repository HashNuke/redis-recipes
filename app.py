from flask import Flask, abort, request
from datetime import datetime
from flask import jsonify
from functools import wraps

app = Flask(__name__)


def throttle_request(function):
    def wrapper():
        user_id = request.args.get('user_id')
        # Block anonymous requests
        if user_id == None:
            return abort(503, "blocked anonymous request. Please pass user_id.")

        # Block a particular user_id
        if user_id == "1":
            abort(503, "Blocked for user")

        return function()
    return wrapper



@app.route('/')
def index():
    return "The world's best example API server"


@app.route('/api/date')
@throttle_request
def date():
    readable_timestamp = str(datetime.now())
    response = {'now': readable_timestamp}
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
