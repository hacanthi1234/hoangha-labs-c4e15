from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello') #hello xuất hiện sau đường link index
def hello():
    return "Hello C4E15"

@app.route('/hellohh')
def hellohh():
    return "Hello Hardihoon"

@app.route('/sayhi/<name>')
def sayhi(name):
    return "Hi " + name

@app.route('/sum/<int:a>/<int:b>')
def sum(a,b):
    return str(a + b)

@app.route('/html')
def heading():
    return "<h1>whatever</h1>"

@app.route('/blog')
def blog():
    posts = [
    {"Content": "Phấn khởi",
     "author": "Hà"},

    {
         "Content": "Phấn khởi",
          "author": "Hà"
    },


    {
        "Content": "Phấn khởi",
        "author": "Hà"
    },


    ]

    article_name = 'Hà đz'
    return render_template('blog.html', article_title= article_name, posts = posts)

if __name__ == '__main__': #luôn phải để cuối
  app.run( debug=True)
