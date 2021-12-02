from request_forest import *
from gini_request import gini_dict

poverty_dict = {'New Hampshire':	7.3,
'Utah':	8.9,
'Maryland':	9.0,
'Minnesota':	9.0,
'New Jersey':	9.2,
'Colorado':	9.3,
'Hawaii':	9.3,
'Massachusetts':	9.4,
'Washington':	9.8,
'Virginia':	9.9,
'Nebraska':	9.9,
'Connecticut':	10.0,
'Alaska':	10.1,
'Wyoming':	10.1,
'United States': 11.7,
'Vermont':	10.2,
'Wisconsin':	10.4,
'North Dakota':	10.6,
'Rhode Island':	10.8,
'Maine':	10.9,
'Idaho':	11.2,
'Iowa':	11.2,
'Delaware':	11.3,
'Kansas':	11.4,
'Oregon':	11.4,
'Illinois':	11.5,
'California':	11.8,
'Indiana':	11.9,
'South Dakota':	11.9,
'Pennsylvania':	12.0,
'Nevada':	12.5,
'Montana':	12.6,
'Florida':	12.7,
'Missouri':	12.9,
'Michigan':	13.0,
'New York':	13.0,
'Ohio':3.1,
'Arizona':	13.5,
'Georgia':	13.3,
'District of Columbia':	13.5,
'North Carolina':	13.6,
'Texas':	13.6,
'South Carolina':3.8,
'Tennessee':	13.9,
'Oklahoma':	15.2,
'Alabama':	15.5,
'West Virginia':	16.0,
'Arkansas':	16.2,
'Kentucky':	16.3,
'New Mexico':	18.2,
'Louisiana':	19.0,
'Mississippi':	19.6}

def generate_table():
    ###Create table structure
    table = []
    for i in range(0, len(gini_dict)):
        table.append([])
    list_of_states = list(gini_dict.keys())
    list_of_states.sort()
    return table

def populate_table(table):
    #populate table using the dictionaries
    row_counter = 0
    for state in list_of_states:
        table[row_counter].append(state)
        table[row_counter].append(gini_dict[state])
        poverty_rate = str(poverty_dict[state]) + "%"
        table[row_counter].append(poverty_rate)
        # get forest density data for state
        forest_data = get_forest_data(state)
        state_requested = forest_data[0]
        forest_density = forest_data[1]
        table[row_counter].append(forest_density)
        row_counter += 1
    table.sort()
    return table


