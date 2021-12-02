import os
from wealth_data import *

def gini_request():
    result = ""
    try:
        request = open("wealth_request.csv", "r")
    except FileNotFoundError:
        return
    for line in request:
        result += line
    print(result)
    return result


def gini_response(request):
    try:
        send_response(request)
    except KeyError:
        send_error()
    delete_file()


def send_response(request_text):
    request_text = request_text.title()
    data = str(gini_dict[request_text])
    with open("wealth_response.csv", "w") as response:
        response.write(data)
    response.close()


def send_error():
    error_message = "You have submitted an invalid input. Please write and send a csv file that conatins ONLY the name " \
                    "of the state you are trying to request data for."
    with open("wealth_response.csv", "w") as response:
        response.write(error_message)
    response.close()

def delete_file():
    try:
        os.remove("wealth_request.csv")
    except FileNotFoundError:
       pass


request = gini_request()
gini_response(request)
