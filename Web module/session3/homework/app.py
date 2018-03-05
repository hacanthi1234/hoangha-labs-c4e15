from flask import *
import mlab
mlab.connect()
from models.service import Service


app = Flask(__name__)


@app.route('/')
def index():
    all_services = Service.objects()
    return render_template('index.html', all_services= all_services)\

@app.route('/detail/<service_id>')
def detail(service_id):
    detail = Service.objects().with_id(service_id)
    return render_template('detail.html', detail= detail)

@app.route('/new_service', methods= ['GET','POST'])
def create():
    if request.method == 'GET':
        return render_template('new_service.html')
    elif request.method == 'POST':

        form = request.form
        name = form['name']
        yob = form['yob']
        phone = form['phone']
        gender = form['gender']

        new_service = Service(name = name,
                                yob = yob,
                                phone = phone,
                                gender = gender,)
        new_service.save()
        return "Saved"



if __name__ == '__main__':
  app.run(debug=True)
