from app import app
from flask import render_template
from app.forms import Phonebook
from app.models import Phone

@app.route('/')
def index():
    phone_info = {
        'name':'Brian',
        'phonenumber':'847-123-4567',
        'address':'123 Fake St, Chicago, IL 98989'
    }
    return render_template('index.html',phone=phone_info)


@app.route('/register', methods=["GET","POST"])
def register():
    form = Phonebook()
    # if the form is submitted and all the data is valid
    if form.validate_on_submit():
        print('Form has been validated! Hooray!!!!')
        name = form.name.data
        phonenumber = form.phonenumber.data
        address = form.address.data
        new_phone = Phone(name=name, phonenumber=phonenumber, address=address)
    return render_template('register.html',form=form)