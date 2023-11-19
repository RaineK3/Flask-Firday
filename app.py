from flask import Flask, render_template

#create a flask instance 
app = Flask(__name__)

#create a route decorator 
@app.route('/')
def index():
  return render_template("index.html")

@app.route('/user/<name>')
def user(name):
  return "<h1>Hello {}</h1>".format(name)

if __name__ == "__main__":
    app.run(debug=True)