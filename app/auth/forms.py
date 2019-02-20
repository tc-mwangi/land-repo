from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, PasswordField,BooleanField
from wtforms.validators import Required,Email,EqualTo
from ..models import User
from wtforms import ValidationError

class LoginForm(FlaskForm):
	email = StringField('Your Email Address',validators=[Required(),Email()], render_kw={"placeholder": "Enter Your Email"})
	password = PasswordField('Password',validators =[Required()], render_kw={"placeholder": "Enter Your Password"})
	remember = BooleanField('Remember me')
	submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    email = StringField('Your Email Address',validators=[Required(),Email()], render_kw={"placeholder": "Your Email Address"})
    name = StringField('Enter your name',validators = [Required()], render_kw={"placeholder": "Your Full Name"})
    username = StringField('Enter your username',validators = [Required()], render_kw={"placeholder": "Enter a Username"})
    password = PasswordField('Password',validators = [Required(), EqualTo('password_confirm',message = 'Passwords must match')], render_kw={"placeholder": "Enter a Password"})
    password_confirm = PasswordField('Confirm Passwords',validators = [Required()], render_kw={"placeholder": "Confirm Password"})
    submit = SubmitField('Sign Up')

    def validate_email(self,data_field):
        if User.query.filter_by(email =data_field.data).first():
            raise ValidationError('There is no account with that email')
    def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('That username is taken')