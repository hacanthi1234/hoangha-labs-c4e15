from flask import Flask, render_template
from models.customer import Customer
import mlab

mlab.connect()

app = Flask(__name__)


@app.route('/<find_id>')
def search(find_id):
    customer = Customer.objects.get(id = find_id)
    return render_template('find_id.html', customer = customer)

if __name__ == '__main__':
  app.run(debug=True)
