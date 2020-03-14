from django.forms import *
from.models import *


class AddFilmForm (ModelForm):
    class Meta:
        model = Film
        fields = '__all__'
        widgets = {
            'title': TextInput({'class': 'form-control'}),
            'country': Select({'class': 'form-control'}),
            'director': Select({'class': 'form-control'}),
            'category': CheckboxSelectMultiple(),
            'release_date': DateInput({'class': 'form-control', 'type': 'date'}),
        }


class AddDirectorForm(ModelForm):
    class Meta:
        model = Director
        fields = '__all__'
        widgets = {
            'first_name':TextInput({'class': 'form-control'}),
            'last_name':TextInput({'class': 'form-control'}),
        }

class AddCommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['comment']
        widgets = {
            'comment':Textarea({'class':'form-control'}),
        }