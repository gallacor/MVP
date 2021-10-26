import csv
import random

def request_forest_data(state):
    with open('state.csv', 'w', newline='') as csvfile:
        written_file = csv.writer(csvfile, delimiter=',')
        written_file.writerow(str(random.random()))
        print(written_file)

def response_forest_data():
    with open('state.csv', newline='') as csvfile:
        file_reader = csv.reader(csvfile, delimiter=',')
        for row in file_reader:
            print(row)
            answer = ''.join(row)
            print(answer)
            return answer
