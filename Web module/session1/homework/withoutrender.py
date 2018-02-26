from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/bmi/<weight>/<height>') #weight(kg), height(cm)
def BMI():
    bmi = float(weight)/ float(((height/100)**2))
    if bmi < 16:
        result = 'severelyUnderweight'
    elif 16<= bmi <18.5:
        result = 'Underweight'
    elif 18.5<= bmi < 25:
        result = 'Normal'
    elif 25 <= BMI < 30:
        result = 'Overweight'
    else:
        result = "Obese"



    return ('BMI =', BMI, ":", result)

if __name__ == '__main__':
  app.run(debug=True)
