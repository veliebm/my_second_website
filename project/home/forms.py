from flask_wtf import Form
from wtforms import TextField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class MessageForm(Form):
    title = TextField("Title", validators=[DataRequired()])
    description = TextAreaField("Description", validators=[DataRequired(), Length(max=140)])
