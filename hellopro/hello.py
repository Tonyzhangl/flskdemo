from flask import Flask, request, redirect, render_template
from flask.ext.script import Manager

app = Flask(__name__)
manager = Manager(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/redirect')
def redict():
    return redirect("http://www.baidu.com")

@app.route('/hello')
def hello():
    return 'Hello World'

@app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' % post_id

@app.route('/projects/')
def projects():
    return 'The projcet page'

@app.route('/about')
def about():
    return 'The about page'

if __name__ == '__main__':
    manager.run()
