from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField 
from wtforms.validators import DataRequired, Length, Email, EqualTo

class LoginForm(FlaskForm):
	username = StringField('Username',validators=[DataRequired()])
	password = PasswordField('Password',validators=[DataRequired(),Length(min=8)])
	# email = StringField('Email',validators=[DataRequired(),Email()])
	remember = BooleanField('Remember me')
	submit = SubmitField('Login')
		
class RegistrationForm(FlaskForm):
	username = StringField('Username',validators = [DataRequired(),Length(min=2,max=20)])
	email = StringField('Email',validators=[DataRequired(),Length(min=8),Email()])
	password = PasswordField('Password',validators=[DataRequired()])
	confirm_password = PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')])
	submit = SubmitField('Sign Up')
