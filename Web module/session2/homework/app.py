from flask import Flask, render_template
from models.customer import Customer

import mlab
mlab.connect()

app = Flask(__name__)



@app.route('/customer')
def index():
    all_customers = Customer.objects()
    return render_template('customer.html', all_customers = all_customers)

@app.route('/10male')
def list():
    customerlist = Customer.objects(gender= 'male', contacted= "not_yet_contacted")
    customerlist2 = customerlist[0:10]
    return render_template('index.html', customerslist2= customerlist[0:10])


if __name__ == '__main__':
  app.run(debug=True)
