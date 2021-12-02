import os

gini_dict = {'Utah':	0.4063,
'Alaska':	0.4081,
'New Hampshire':	0.4304,
'Wyoming'	:0.4360,
'Hawaii'	:0.4420,
'Iowa'	:0.4451,
'Nebraska'	:0.4477,
'South Dakota':	0.4495,
'Minnesota':	0.4496,
'Wisconsin'	:0.4498,
'Maryland'	:0.4499,
'Idaho'	:0.4503,
'Maine'	:0.4519,
'Delaware':	0.4522,
'Indiana':	0.4527,
'North Dakota':	0.4533,
'Vermont':	0.4539,
'Kansas':	0.4550,
'Nevada':	0.4577,
'Oregon'	:0.4583,
'Colorado':	0.4586,
'Washington':	0.4591,
'Oklahoma':	0.4645,
"Missouri":	0.4646,
"Montana":	0.4667,
"Ohio":	0.4680,
"Pennsylvania":	0.4689,
"Michigan":	0.4695,
"Virginia":	0.4705,
"West Virginia":	0.4711,
"Arizona":	0.4713,
"Arkansas":	0.4719,
"South Carolina":	0.4735,
"New Mexico":	0.4769,
"North Carolina":	0.4780,
"Rhode Island":	0.4781,
"Massachusetts":	0.4786,
"Tennessee":	0.4790,
"Texas":	0.4800,
"Illinois":	0.4810,
"New Jersey":	0.4813,
"Kentucky":	0.4813,
"Georgia":	0.4813,
"Mississippi":	0.4828,
"Alabama":	0.4847,
"Florida":	0.4852,
"California":	0.4899,
"Connecticut":	0.4945,
"Louisiana":	0.4990,
"New York":	0.5229,
"Washington DC":	0.5420 }

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
