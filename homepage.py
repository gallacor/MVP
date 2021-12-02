from request_forest import *
from wealth_data import *


def generate_table():
    ###Create table structure
    table = []
    for i in range(0, len(gini_dict)):
        table.append([])
    list_of_states = list(gini_dict.keys())
    list_of_states.sort()
    return table, list_of_states

def populate_table(table, list_of_states):
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


