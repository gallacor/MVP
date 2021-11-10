from request_forest import *
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
"New York":	0.5229 }

def create_table():
    #create table the length of the dictionaries
    table = []
    for i in range(0, len(gini_dict)):
        table.append([])
    #populate table using the dictionaries
    row_counter = 0
    list_of_states = list(gini_dict.keys())
    list_of_states.sort()
    print(list_of_states)
    for state in list_of_states:
        table[row_counter].append(state)
        table[row_counter].append(gini_dict[state])
        poverty_rate = str(poverty_dict[state]) + "%"
        table[row_counter].append(poverty_rate)
        # get forest density data for state
        forest_data = get_forest_data(state)
        state_requested = forest_data[0]
        forest_density = forest_data[1]
        print(state_requested + " " + forest_density)
        table[row_counter].append(forest_density)
        row_counter += 1
    table.sort()
    return table


