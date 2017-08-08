from flask import Flask
from flask import render_template
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    #read file
    file = open('test.json', 'r+') #sdaf
    file_text = file.read()
    file_text = dict(json.loads(file_text))
    return render_template('test.html',data=file_text)

@app.route('/details/<string:student_number>')
def details(student_number):
    return render_template( str(student_number) + '.html')

if __name__ == '__main__':
    app.run(debug=True)