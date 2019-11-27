from flask_wtf import FlaskForm
from wtforms import StringField ,PasswordField ,SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(),Length(min=4, max = 18)])
    email = StringField('Email', validators=[DataRequired(),Email()])
    password = PasswordField('password', validators=[DataRequired()])
    confirm_password = PasswordField('confirm_password', validators=[DataRequired(),EqualTo('password')]) 
    submit = SubmitField('sign up') 
    


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us more  about you.',validators = [DataRequired()])
    submit = SubmitField('Submit')
    
    
class PostForm(FlaskForm):
     title = StringField('Title', validators=[DataRequired()])
     content = TextAreaField('Content',validators=[DataRequired()])
     submit = SubmitField('Post')