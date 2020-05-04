# login form created with flask_wtf

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length
from app.models import User
from flask_babel import _, lazy_gettext as _lg    # lazy language translation
                                                  # translation done when string is used
class LoginForm(FlaskForm):
    username = StringField(_lg('Username'), validators=[DataRequired()])
    password = PasswordField(_lg('Password'), validators=[DataRequired()])
    remember_me = BooleanField(_lg('Remember me'))
    submit = SubmitField(_lg('Sign In'))


class RegistrationForm(FlaskForm):          # user registration form
    username = StringField(_lg('Username'), validators=[DataRequired()])
    email = StringField(_lg('Email'), validators=[DataRequired(), Email()])  # email validator to confirm email is indeed an email address
    password = PasswordField(_lg('Password'), validators=[DataRequired()])
    password2 = PasswordField(_lg('Repeat Password'), validators=[DataRequired(), EqualTo('password')])  # validator to confirm 2nd input of password matches
    submit = SubmitField(_lg('Register'))

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError(_('Please use a different username.'))

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError(_('Please use a different email address.'))


class ResetPasswordRequestForm(FlaskForm):
    email = StringField(_lg('Email'), validators=[DataRequired(), Email()])
    submit = SubmitField(_lg('Request Password Reset'))


class ResetPasswordForm(FlaskForm):
    password = PasswordField(_lg('Password'), validators=[DataRequired()])
    password2 =  PasswordField(_lg('Confirm password'), validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField(_lg('Request password reset'))
