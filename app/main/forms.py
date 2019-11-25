from flask_wtf import FlaskForm
from wtforms import StringField ,PasswordField ,SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(),Length(min=4, max = 18)])
    email = StringField('Email', validators=[DataRequired(),Email()])
    password = PasswordField('password', validators=[DataRequired()])
    confirm_password = PasswordField('confirm_password', validators=[DataRequired(),EqualTo('password')]) 
    submit = SubmitField('sign up') 
    
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),Email()])
    password = PasswordField('password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('login') 
    