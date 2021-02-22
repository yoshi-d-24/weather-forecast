import json

import requests

PORT: int = 8082
URL: str = f'http://localhost:{PORT}/2015-03-31/functions/function/invocations'


def call(url):
    res = requests.post(
        url,
        json.dumps({}).encode('utf-8'),
        headers={'Content-Type': 'application/json'})
    print(res.json())


if __name__ == '__main__':
    call(url=URL)
