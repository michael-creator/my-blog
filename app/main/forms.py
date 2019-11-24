from flask_wtf import FlaskForm
from wtforms import StrinField ,PasswordField ,SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    username = StrinField('username', validators=[DataRequired(),Length(min=4, max = 18)])
    email = StrinField('Email', validators=[DataRequired(),Email()])
    password = passwordField('password', validators=[DataRequired()])
    confirm_password = passwordField('confirm_password', validators=[DataRequired(),EqualTo('password')]) 
    submit = SubmitField('sign up') 
    
class LoginForm(FlaskForm):
    email = StrinField('Email', validators=[DataRequired(),Email()])
    password = passwordField('password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('login') 
    