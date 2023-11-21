from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

#create a flask instance 
app = Flask(__name__)
app.config['SECRET_KEY'] = "I'm so handsome"

#create a Form Class
class NameForm(FlaskForm):
  name = StringField("What's Your Name", validators=[DataRequired()])
  submit = SubmitField("Submit")

#create a route decorator 
@app.route('/')
def index():
  flash("Welcome To Our Website!")
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
def page_not_found(e):
  return render_template("500.html"),500

#create name page
@app.route('/name', methods=['GET', 'POST'])
def name():
   name = None
   form = NameForm()
   #validate form
   if form.validate_on_submit():
     name = form.name.data
     form.name.data = ''
     flash("Form Submitted Successfully!")
   return render_template("name.html",
                          name = name,
                          form = form)

if __name__ == "__main__":
    app.run(debug=True)