# regular imports for flask-wtf
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import EqualTo, DataRequired, Length, ValidationError

# for user validation
from app.models import User
from app.extensions import bcrypt


class RegisterForm(FlaskForm):
    username = StringField(label="Username",
                         validators=[DataRequired(), Length(min=3, max=50)])
    password1 = PasswordField(label="Password",
                         validators=[DataRequired(), Length(min=6, max=50)])
    password2 = PasswordField(label="Confirm Password",
                         validators=[
                             DataRequired(),
                             Length(min=6, max=50),
                             EqualTo("password1")])
    submit = SubmitField(label="Sign Up")

    
    # validate password match
    def validate_password2(self, affirm_password):
        if affirm_password.data != self.password1.data:
            raise ValidationError("Passwords don't match!!!")

    
    # validate username availability
    def validate_username(self, username):
        user = User.query.filter(User.username==username.data).first()
        if user:
            raise ValidationError("User already exists!")
        elif username.data.lower() == "guest" \
                                or username.data.lower() == "anonymous":
            raise ValidationError(f"Username: {username.data} prohibited!")
    

class LoginForm(FlaskForm):
    username = StringField(label="Username", validators=[DataRequired()])
    password = PasswordField(label="Password", validators=[DataRequired()])
    remember_me = BooleanField(label="Stay logged in")
    submit = SubmitField(label="Login")


    # validate account existence
    def validate_username(self, username):
        user = User.query.filter(User.username == username.data).first()
        if user and bcrypt.check_password_hash(user.password, self.password.data):
            pass
        else:
            raise ValidationError(f"No account with such credentials exists!")
            