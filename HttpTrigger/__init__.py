import logging

import azure.functions as func
import requests


def main(req: func.HttpRequest) -> func.HttpResponse:
    url = "http://20.187.114.37:86/data"

    response = requests.get(url).text

    logging.info(
        'Python HTTP trigger function processed a request,response: %s', response)

    return func.HttpResponse(
        f"Hello, this message from Azure : {response}",
        status_code=200
    )
