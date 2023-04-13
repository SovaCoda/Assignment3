from flask import Flask, render_template, request
from bmi import calculateBMI, classify
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    output = None

    if request.method == 'POST':
        weight = int(request.form['weight_input'])
        height = int(request.form['height_input'])
        bmi = round(calculateBMI(weight, height), 2)
        classification = classify(bmi)
        output = f'Your BMI is {bmi} and you are {classification}'
    
    return render_template('main.html', output=output)

if __name__ == '__main__':
    app.run(debug=True)
