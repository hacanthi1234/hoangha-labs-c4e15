from flask import Flask, render_template
from models.customer import Customer
import mlab

mlab.connect()

app = Flask(__name__)

id_to_find = "5a9857929e06832cd04b0f31"
document = Customer.objects.get(id = id_to_find)


document.delete(id_to_find)


# @app.route('/<find_id>')
# def search(find_id):
#     customer = Customer.objects.get(id = find_id)
#     return render_template('find_id.html', customer = customer)
#
# if __name__ == '__main__':
#   app.run(debug=True)
