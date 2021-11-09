import csv
import random
import os

# def request_forest_data(state):
#     with open('state.csv', 'w', newline='') as csvfile:
#         written_file = csv.writer(csvfile, delimiter=',')
#         written_file.writerow(str(random.random()))
#         print(written_file)
#
# def response_forest_data():
#     with open('state.csv', newline='') as csvfile:
#         file_reader = csv.reader(csvfile, delimiter=',')
#         for row in file_reader:
#             print(row)
#             answer = ''.join(row)
#             print(answer)
#             return answer
#
def request_wealth_data(state):
    with open('wealth_request.csv', 'w') as request:
        request.write(state)

request_wealth_data("New York")
os.system('python gini_request.py')