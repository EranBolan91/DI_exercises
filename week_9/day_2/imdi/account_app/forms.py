from django.forms import *

class SignUpForm(Form):
    username = CharField(required=True,max_length=50,widget=TextInput(attrs={'class':'form-control'}))
    password = CharField(required=True,widget=PasswordInput(attrs={'class':'form-control'}))
    email = EmailField(required=True, widget=EmailInput(attrs={'class':'form-control'}))
    first_name = CharField(widget=TextInput(attrs={'class':'form-control'}))
    last_name = CharField(widget=TextInput(attrs={'class':'form-control'}))


class LoginForm(Form):
    username = CharField(required=True,widget=TextInput(attrs={'class':'form-control'}))
    password = CharField(required=True, widget=PasswordInput(attrs={'class':'form-control'}))