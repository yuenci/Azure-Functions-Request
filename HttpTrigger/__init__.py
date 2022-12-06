import logging

import azure.functions as func
import requests


def main(req: func.HttpRequest) -> func.HttpResponse:
    req_body_bytes = req.get_body()

    # send a get post to the url
    url = "http://101.43.138.40:9898/data"
    response = requests.get(url)
    logging.info(
        'Python HTTP trigger function processed a request: response: %s', response.text)

    return func.HttpResponse(
        f"Hello, this message from Azure : {response.text}",
        status_code=200
    )
