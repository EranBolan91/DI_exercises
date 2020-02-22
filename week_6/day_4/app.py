from flask import Flask ,render_template,redirect,url_for,request,flash
from pets_class import Pet
from cart_class import Cart
from user_class import User
from form import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/pets')
def pets():
    pets = Pet()
    data = pets.getAllPets()
    return render_template('pets.html',pets=data)

@app.route('/cart')
def cart():
    cart = Cart()
    data = cart.get_cart()
    total_sum = cart.get_total_sum(data)
    return render_template('cart.html',carts=data,total_sum=total_sum)

@app.route('/cart/<cartid>')
def cart_remove(cartid):
    cart = Cart()
    cart.remove_item(cartid)
    return redirect(url_for('pets'))

@app.route('/pets/<petid>')
def pet_display(petid):
    pet = Pet()
    data = pet.getPet(petid)
    return render_template('pet.html',pet=data)

@app.route('/addpet/<petid>')
def add_pet(petid):
    pets = Pet()
    cart = Cart()
    data = pets.getPet(petid)
    pet_details = {'id': data['id'], 'price': data['price'], 'image': data['image'], 'quantity': 1}
    cart.add_to_cart(pet_details)
    return redirect(url_for('pets'))

@app.route('/login',methods=["GET","POST"])
def login():
    if request.method == "GET":
        return render_template('login.html')

    if request.method == "POST":
        user = User()
        email = request.form['email']
        password = request.form['password']
        if user.login(email,password):
            flash("Successful log in")
            return redirect(url_for('home'))
        else:
            flash("Wrong deatils")
            return redirect(url_for('login'))

@app.route('/register', methods=["GET","POST"])
def register():
    form = Form()
    if request.method == "GET":
        return render_template('register.html',form=form)

    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        user = User()
        user.save_user_in_db(name,email,password)
        return render_template('login.html')


if __name__ == '__main__':
    app.run()
