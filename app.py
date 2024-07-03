from flask import Flask, render_template, request, jsonify
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_form', methods=['POST'])
def process_form():
    name = request.form['name']
    birthdate = request.form['birthdate']

    birthdate = datetime.datetime.strptime(birthdate, '%Y-%m-%d').date()
    today = datetime.date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

    response = {
        'name': name,
        'birthdate': birthdate.strftime('%Y-%m-%d'),
        'age': age
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)