from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/original/api/data')
def get_data():
    response = jsonify({'message': 'Hello from Flask!'})
    response.set_cookie('example', 'value', secure=True, samesite='None')
    return response


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=9999, debug=True)
