from flask import Flask, render_template, request, url_for
from homepage import *
from request_forest import *

app = Flask(__name__, template_folder="templates")
app.static_folder = 'static'
@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route("/state_data", methods=['POST'])
def state_data():
    return state_page()

def state_page():
    state = request.form["state"]
    print(state)
    poverty_rate = poverty_dict[state]
    gini_index = gini_dict[state]
    response_data = get_forest_data(state)
    forest_density = response_data[1]
    return render_template('state_page.html', poverty_rate=poverty_rate, gini_index=gini_index, state=state, forest_density=forest_density)

@app.route("/country_view", methods=['POST'])
def country_view():
        return country_page_unsorted()


def country_page_unsorted():
    table = create_table()
    return render_template('country_page.html', table=table)




if __name__ == '__main__':
    app.run(debug=True,
            port=5000)