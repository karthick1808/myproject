import requests
from prometheus_client import start_http_server, Summary

REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

@REQUEST_TIME.time()
def make_request():
    response = requests.get("https://www.example.com")
    return response.status_code

if __name__ == "__main__":
    start_http_server(8000)
    while True:
        make_request()
