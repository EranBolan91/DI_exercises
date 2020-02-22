import flask_wtf
import wtforms
from wtforms import validators,FileField



def validate_price(form,field):
    if field.data < 0:
       raise wtforms.ValidationError('Price cant be lower then 0')

class Form(flask_wtf.FlaskForm):

    name = wtforms.StringField("Name", [validators.Length(min=4, max=20,message="name must be between 4 - 20"), validators.InputRequired()])
    email = wtforms.StringField("Price", [validators.data_required(),validators.Email(message="email not")])
    password = wtforms.PasswordField("Password",[validators.data_required()])
    confirm_password = wtforms.PasswordField("Confirm password", [validators.data_required()])
    #photo = FileField(validators=[FileAllowed(ALLOWED_EXTENSIONS, 'Image only!'), FileRequired('File was empty!')])
    image = FileField('image')
    btn_submit = wtforms.SubmitField("Register")
