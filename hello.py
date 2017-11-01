from flask import Flask, render_template
import sys

app = Flask(__name__)

@app.route("/")
def index():
  data=['Rossiter House','The Main Entryway','red',app.instance_path,app.root_path,sys.version]
  return render_template('home.html',data=data)

@app.route("/library")
def library():
  # This page will need database access.
  # Much code can be pulled from previous DCPL implementation!
  data=['Library Page','Hello, World!','blue with chocolate chimps',app.instance_path,app.root_path]
  return render_template('library.html',data=data)

@app.route('/user/<username>')
def show_user(username):
    # show the user profile for that user
    return 'User %s is the best user.' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d, come in.' % post_id

@app.route('/countdown')
def countdown():
    return render_template('index.html')

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
