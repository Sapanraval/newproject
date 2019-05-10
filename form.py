from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email


class ContactForm(FlaskForm):
    name = StringField('Name',validators=[DataRequired(),])
    email = StringField('Email',validators=[DataRequired(), Email()])
    subject = StringField('Subject',validators=[DataRequired()])    
    message = TextAreaField('Message', validators=[DataRequired()])
    submit = SubmitField('Submit')