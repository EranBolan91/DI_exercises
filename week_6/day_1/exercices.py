from datetime import date
from flask import Flask
from pizza import make_pizza
from flask import render_template, render_template_string

app = Flask(__name__)

@app.route('/')
def hello_world():
    today = str(date.today())
    html = render_template('index.html', date=today)
    return html

@app.route('/home')
def create_pizza():
    return make_pizza()

@app.route('/cv/<string:name>/<string:profile_picture>/<string:skills>/<string:strengths>/<string:weaknesses>')
def display_cv(name,profile_picture,skills,strengths,weaknesses):
    html = render_template('cv.html',name=name,picture=profile_picture,hobbies=skills,strengths=strengths,weaknesses=weaknesses)
    return html

if __name__ == "__main__":
    app.run(debug=True)
