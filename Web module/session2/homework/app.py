from flask import Flask, render_template
from models.customer import Customer

import mlab
mlab.connect()

app = Flask(__name__)



@app.route('/customer')
def index():
    all_customers = Customer.objects()
    return render_template('customer.html', all_customers = all_customers)




if __name__ == '__main__':
  app.run(debug=True)
