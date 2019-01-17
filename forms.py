from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class SignupForm(Form):
    first_name = StringField('First name', validators=[DataRequired("silahkan masukan nama pertama")])
    last_name = StringField('Last name', validators=[DataRequired("silahkan masukan nama terakhir")])
    email = StringField('Email', validators=[DataRequired("silahkan masukan email"), Email("give correct email !")])
    password = PasswordField('Password', validators=[DataRequired("silahkan masukan password"), Length(min=6, message="password must be 6 characters")])
    submit = SubmitField('Sign up')

class LoginForm(Form):
    email = StringField('Email', validators=[DataRequired("please enter your email address."), Email("please enter your email again.")])
    password = PasswordField('password', validators=[DataRequired("Please enter a password")])
    submit = SubmitField("sign in")

class AddressForm(Form):
    address = StringField('Address', validators=[DataRequired('please enter an address.')])
    submit = SubmitField('Search')

