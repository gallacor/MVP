from flask import Flask, render_template, request, url_for
from homepage import *
from dummydata_creator import *

app = Flask(__name__, template_folder="templates")

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route("/state_or_country", methods=['POST'])
def state_or_country():
    try:
        if request.form["country"] == "True":
            return country_page_unsorted()
    except KeyError:
        return state_page()

def state_page():
    state = request.form["state"]
    print(state)
    poverty_rate = poverty_dict[state]
    gini_index = gini_dict[state]
    request_forest_data(state)
    forest_density = str(response_forest_data())
    return render_template('state_page.html', poverty_rate=poverty_rate, gini_index=gini_index, state=state, forest_density=forest_density)


def country_page_unsorted():
    # create matrix for 50 states data and generate table
    test = "testing"
    request_forest_data(test)
    table = create_table()
    forest_density = str(response_forest_data())
    return render_template('country_page.html', table=table, forest_density=forest_density)




if __name__ == '__main__':
    app.run(debug=True,
            port=5000)