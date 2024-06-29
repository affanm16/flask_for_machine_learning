from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    SelectField,
    DateField,
    PasswordField,
    SubmitField,
    BooleanField
)


from wtforms.validators import (
    DataRequired,
    Length,
    Email,
    Optional,
    EqualTo
)



class SignupForm(FlaskForm):
    username=StringField(
        "USERNAME",
        validators=[DataRequired(),Length(min=5,max=30)]   
    )
    email=StringField(
        "EMAIL",
        validators=[DataRequired(),Email()]
    )
    gender=SelectField(
        "GENDER",
        choices=["Male","Female","others"],
        validators=[Optional()]
    )
    dob=DateField(
        "DATE OF BIRTH",
        validators=[Optional()]
    )
    password=PasswordField(
        "PASSWORD",
        validators=[DataRequired(),Length(min=8,max=25)]
    )
    confirm_password=PasswordField(
        "CONFIRM PASSWORD",
        validators=[DataRequired(),Length(min=8,max=25),EqualTo("password")]
    )
    submit=SubmitField("SIGN UP")

  





class LoginForm(FlaskForm):
    email=StringField(
        "EMAIL",
        validators=[DataRequired(),Email()]
    )
    password=PasswordField(
        "PASSWORD",
        validators=[DataRequired(),Length(8,25)]
    )
    remember_me =BooleanField("REMEMBER ME")
    submit=SubmitField("LOGIN")
