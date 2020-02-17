from flask import Flask
from flask import render_template
from flask import request
from datetime import datetime,time
import db

app = Flask(__name__)

@app.route('/')
def home():
    sentence = ""
    now = datetime.now()
    now_time = now.time()
    if now_time >= time(8) and now_time <= time(13):
        sentence = "Good morning"
    elif now_time >= time(13) and now_time <= time(17):
        sentence = "Good afternoon"
    elif now_time >= time(17) and now_time <= time(21):
        sentence = "Good evening"
    elif now_time >= time(21) and now_time <= time(8):
        sentence = "Good night"

    return render_template('home.html',greeting=sentence)

@app.route('/products')
def products():
    data = db.load_products()
    return render_template('products.html',products_list=data)

@app.route('/product/<string:id>')
def product_display(id):
    data = db.load_products()
    product = {}
    for item in data:
        if item['ProductId'] == id:
            product = item
    return render_template('product_details.html',product=product)



if __name__ == "__main__":
    app.run()