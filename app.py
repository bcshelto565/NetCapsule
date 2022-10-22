from collections import defaultdict

import requests
from flask import Flask, render_template, request
import datetime
from dateutil import parser

app = Flask(__name__)


def get_header():
    headers = {
        'Authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI3MmZlOGFmOTAwNjUxOGNmZDQwMmQxODlhNDYxYmQzYyIsImp0aSI6IjUyN2YzZjQxZTM2OGY3M2I4NzRlZWQ3NmU0YzE4YWExN2ZlZGI3M2IxYWJjNTFlZWI4MjkwMGE5NDI3MDRkODc1NTkyYTVkMzkyMDU5OTU5IiwiaWF0IjoxNjY2NDI0NzQ2LjIxMDE3OCwibmJmIjoxNjY2NDI0NzQ2LjIxMDE4MywiZXhwIjozMzIyMzMzMzU0Ni4yMDg0NTgsInN1YiI6IjcwOTgxMzA0IiwiaXNzIjoiaHR0cHM6Ly9tZXRhLndpa2ltZWRpYS5vcmciLCJyYXRlbGltaXQiOnsicmVxdWVzdHNfcGVyX3VuaXQiOjUwMDAsInVuaXQiOiJIT1VSIn0sInNjb3BlcyI6WyJiYXNpYyJdfQ.egiyPFxIge7FJ6gMsmCzHs3asIGjPrs3KkwOUNb7Vyjub3dzCB1CJBj7piNMplSr9CLAeVsWam9EXzK48UkynOuIGwcSVm8MprDWhK94pLowTwvmt1U9JNGbesAj59QTh-QIl4YTLl7_p0K25lhlEQWdC_o_soe5B7DfA5x4vBDbhCP4rnn4bmanxX5QgH31p6NaqKYmSQGe7CbUY8kJCzPXf3jflbvzNnzS0HEh-MnGkPNDMviVWQcRwqs0W5yrLibKc97hROVzEl5gfVnk_Fc5MeV-uXmrTaO1EMdJ_biCov46CLEOU5gcwr_z_uNKV-oYVZlJE9Ztm_OAjISYmXGjw37xh0q49j63sz7zsYiRWtXCKZZY1JIeuEbTHv0TXwZEQ6ImjkK6Mg7A2WErjUYMpNgnQy-eGt9IX2KTaK-IXjdSjPiwfmPixsb5YwlDvQeDOc0xBb_tGgiqbLrG_I36_oqyge-myGbnIvDsx2cqWltpPPMHG-kKvvE_YCYS0oCz-QZB7dapdHwR69sguePhZFdS4oXgN9VM4FIRW_U2kqGLy2AFj0NuHWEDGtVQXLDgDKXsZA8ZE9pxG6FthnQm7J7n2cvoPnyh7Hwa_5pjOOJqWWQW4ls7RkC3wfhObCCROEbYWKKSQS89YXUQm2piSrGzJB7NUrWnel3Yrw8',
        'User-Agent': 'YOUR_APP_NAME (YOUR_EMAIL_OR_CONTACT_PAGE)'
    }
    return headers


def get_data(date):
    url = 'https://api.wikimedia.org/feed/v1/wikipedia/en/onthisday/all/' + date
    response = requests.get(url, headers=get_header())
    data = response.json()
    return data


def today_in_history():
    today = datetime.datetime.now()
    date = today.strftime('%m/%d')
    data = get_data(date)


def that_date_history(selected_date):
    date = selected_date.strftime('%m/%d')
    data = get_data(date)
    return data


@app.route('/that_day')
def select_date():
    return render_template("that_day.html")


@app.route('/')
def home():
    return render_template('index.html')

def filter_data(year,data):
    filtered_data = defaultdict(list)
    for event in data:
        for i in range(len(data[event])):
            if data[event][i]['year'] == year:
                filtered_data['event'].append(data[event][i]['year'])
    return filtered_data

def trim_data(data):
    for event in data:
        data[event] = data[event][:min(len(data[event]),10)]
    return data


@app.route('/that_day_data', methods=['GET', 'POST'])
def day_data():
    select = request.form.get('date_select')
    select_date = parser.parse(select)
    data = that_date_history(select_date)
    data = trim_data(data)
    mm = select_date.strftime("%B")
    dd = select_date.strftime("%d")
    pay_load = [{'mm':mm,'dd':dd}, data]
    return render_template("that_day_data.html", payload=pay_load)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
