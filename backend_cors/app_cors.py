from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)


# CORS(app,
#      resources={r"*": {"origins": "http://localhost"}}, \
#      supports_credentials=True,
#      # allow_headers=["Content-Type", "Accept-Charset", "Accept", "Cookie", "Accept-Encoding", "Accept-Language",
#      #                "Cache-Control", ""],
#      allow_methods="GET,POST,PUT,DELETE", )


@app.route('/cors/api/data', methods=['delete'])
def get_data():
    response = jsonify({'message': 'Delete from Flask!'})
    return response


@app.after_request
def handle_options(response):
    response.headers["Access-Control-Allow-Origin"] = "http://localhost"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization, X-Requested-With, Cookie"
    response.headers["Access-Control-Allow-Credentials"] = "true"

    return response


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8888, ssl_context=('cert.crt', 'cert.key'))
