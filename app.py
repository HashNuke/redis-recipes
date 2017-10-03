from flask import Flask, abort, request, jsonify
from datetime import datetime
from functools import wraps
import rate_limiters

app = Flask(__name__)
rate_limiter = rate_limiters.DummyRateLimiter("dummy_requests", limit_per_minute=100)


def rate_limit(function):
    def wrapper():
        user_id = request.args.get('user_id')
        if rate_limiter.can_allow(user_id):
            return function()
        return abort(503, "Rate limit reached")
    return wrapper


"""
Very simple auth.
Checks for a user_id to be present in the URL.
Blocks anonymous requests with a 503 status.
"""
def authenticate(function):
    def wrapper():
        user_id = request.args.get('user_id')
        if user_id == None:
            return abort(503, "Blocked anonymous request. Please pass user_id in the url")

        return function()
    return wrapper



@app.route('/')
def index():
    return "The world's best example API server"


@app.route('/api/date')
@authenticate
@rate_limit
def date():
    readable_timestamp = str(datetime.now())
    response = {'now': readable_timestamp}
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
