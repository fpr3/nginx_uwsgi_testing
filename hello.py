from flask import Flask,render_template
app = Flask(__name__)

@app.route("/")
def index():
  data=['Index Page','The Main Entryway','red']
  return render_template('template1.html',data=data)

@app.route("/hello")
def hello():
  data=['Hello Page','Hello, World!','blue with chocolate chimps']
  return render_template('template1.html',data=data)

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
