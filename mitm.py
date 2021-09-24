from flask import Flask
import requests
from flask import request
import os
import toml


def read_config():
    with open("conf.toml", "r") as file:
        data = toml.load(file)
        os.environ["host"] = data["host"]


app = Flask(__name__)

def send_request(host, path, headers):
    uri = f"{host}/{path}"
    print(uri)
    response = requests.get(uri, headers=headers, verify=False)
    data = response.content
    http_code = response.status_code
    return data, http_code


def send_post(host, path, header, payload):
    uri = f"{host}/{path}"
    print(uri)
    response = requests.post(uri, json=payload, headers=header, verify=False)
    data = response.content
    http_code = response.status_code
    return data, http_code


@app.route('/', defaults={'path': ''})
@app.route("/<path:path>", methods=['GET'])
def proxy_get(path):
    headers = request.headers
    response, http_code = send_request(os.environ["host"], path, headers)
    return response, http_code


@app.route('/', defaults={'path': ''})
@app.route("/<path:path>", methods=['POST'])
def proxy_post(path):
    headers = request.headers
    payload = request.json
    response, http_code = send_post(os.environ["host"], path, headers, payload)
    return response, http_code


if __name__ == '__main__':
    read_config()
    app.run(host='localhost', port=8080, debug=True)