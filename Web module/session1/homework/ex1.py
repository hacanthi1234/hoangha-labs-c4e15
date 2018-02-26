import os
from flask import Flask, render_template,redirect
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hellohh')
def hellohh():
    return "Hello Hardihoon"

@app.route('/about_me')
def aboutme():
    return render_template('about_me.html')

@app.route('/school')
def school():
    return redirect('http://techkids.vn', code = 302)


if __name__ == '__main__':
  app.run( debug=True)
