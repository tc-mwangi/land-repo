from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, PasswordField,BooleanField,FloatField,SelectField
from wtforms.validators import Required,Email,EqualTo
from ..models import User
from wtforms import ValidationError

class LoginForm(FlaskForm):
	email = StringField('Your Email Address',validators=[Required(),Email()], render_kw={"placeholder": "Enter Your Email"})
	password = PasswordField('Password',validators =[Required()], render_kw={"placeholder": "Enter Your Password"})
	remember = BooleanField('Remember me')
	submit = SubmitField('Log In')

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


class PlaceForm(FlaskForm):
    place = StringField('Name of Place',validators=[Required()], render_kw={"placeholder": "Enter the name of the Place"})
    lat = FloatField('Latitude',validators=[Required()], render_kw={"placeholder": "Enter Latitude"})
    lng = FloatField('Longitude',validators=[Required()], render_kw={"placeholder": "Enter Longitude"})
    region = SelectField('Region',validators=[Required()], choices=[('Nairobi','Nairobi'),('Uasin Gishu','Uasin Gishu'),('Kisumu','Kisumu'),('Kwale','Kwale'),('Moyale','Moyale'),('Mombasa','Mombasa'),('Kilifi','Kilifi'),('Homabay','Homabay')], render_kw={"placeholder": "Enter Region"})
    submit = SubmitField('Submit')