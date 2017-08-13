from flask import Flask
from flask import render_template
import json

app = Flask(__name__)

def read_json_file(filepath):
    jsonfile = open(filepath, 'r+')
    jsontext = jsonfile.read()
    data = json.loads(jsontext)
    jsonfile.close()
    return data    

@app.route('/')
def hello_world():
    data = read_json_file('static/data/index.json')
    return render_template('index.html', data=data)

@app.route('/details/<string:student_number>')
def look_details(student_number):
    data = read_json_file('static/data/index.json')
    user_data = {}
    for item in data:
        if student_number == item['student_number']:
            user_data = item
            break
    print user_data
    return render_template('details.html', data=user_data)

if __name__ == '__main__':
    app.run(debug=True)