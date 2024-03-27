
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, RadioField, TextAreaField, DateTimeField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError,Optional 
from game.models import User


class Register_form(FlaskForm):
    username = StringField(label='username', validators=[Length(min=2, max=30), DataRequired()])
    phone_no = StringField(label='phone_no', validators=[Length(min=10, max=10), DataRequired()])
    email = StringField(label='Email:', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='password', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirm Password:', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Create Account')

    def validate_email(self, field):
        if User.query.filter_by(email_address=field.data).first():
            raise ValidationError('Email already registered.')
        
    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')


class Login_form(FlaskForm):
    email = StringField(label='Email:', validators=[Email(), DataRequired()])
    password = PasswordField(label='Password:', validators=[DataRequired()])
    submit = SubmitField(label='Sign in')


class Booking_form(FlaskForm):

    submit= SubmitField(label='Book session')


