from flask import Flask
import requests
from flask import request
import os


app = Flask(__name__)

def send_request(host, path, headers):
    uri = f"{host}/{path}"
    print(uri)
    response = requests.get(uri)
    data = response.content
    http_code = response.status_code
    return data, http_code


def send_post(host, path, header, payload):
    uri = f"{host}/{path}"
    print(uri)
    response = requests.post(uri, json=payload, headers=header)
    data = response.content
    http_code = response.status_code
    return data, http_code


@app.route('/', defaults={'path': ''})
@app.route("/<path:path>", methods=['GET'])
def proxy_get(path):
    headers = request.headers
    response, http_code = send_request("https://stackblog.io", path, headers)
    return response, http_code


@app.route('/', defaults={'path': ''})
@app.route("/<path:path>", methods=['POST'])
def proxy_post(path):
    headers = request.headers
    payload = request.json
    response, http_code = send_post("https://stackblog.io", path, headers, payload)
    return response, http_code


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)