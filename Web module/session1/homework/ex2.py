from flask import Flask, render_template
app = Flask(__name__)


@app.route('/user/<user_name>')
def user_profile(user_name):
    article_title = 'User_name'
    profiles = {
    'Ha':    {'Name':"hoang ha",
        'Age': 20,
        'Gender': 'nam',
        'Hobby': 'playing board games',
        },

    }
    if user_name in profiles:
        user_info = profiles[user_name]
        return render_template('user_profile.html', article_title = article_title, user_info = user_info)
    else:
        return ('User not found!')
if __name__ == '__main__':
  app.run(debug=True)
