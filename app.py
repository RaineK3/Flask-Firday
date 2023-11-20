from flask import Flask, render_template

#create a flask instance 
app = Flask(__name__)

#create a route decorator 
@app.route('/')
def index():
  return render_template("index.html")

@app.route('/user/<name>')
def user(name):
  return render_template("user.html", username = name)

#create custom error pages

#invalid url
@app.errorhandler(404)
def page_not_found(e):
  return render_template("404.html"),404

#internl server error
@app.errorhandler(500)
 git push -u origin main

if __name__ == "__main__":
    app.run(debug=True)