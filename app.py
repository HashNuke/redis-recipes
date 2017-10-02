from flask import Flask
from datetime import datetime
from flask import jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return "The world's best example API server"


@app.route('/api/date')
def date():
    readable_timestamp = str(datetime.now())
    response = {'now': readable_timestamp}
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
