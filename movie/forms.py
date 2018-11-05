from django import forms
from django.forms import DateInput

class MovieForm(forms.Form):
    title = forms.CharField(label='Title', max_length=50, required=True)
    cover_photo = forms.ImageField(label='Cover', allow_empty_file=False)
    description = forms.CharField(label='Description', widget=forms.Textarea, required=True)
    release_date = forms.DateField(label='Release Date', widget=DateInput(attrs={'type': 'date'}), required=True)
    rating = forms.ChoiceField(label='Rating',choices=(
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ), required=True)


class PersonForm(forms.Form):
    name = forms.CharField(label='Name', max_length=50, required=True)
    photo = forms.ImageField(label='Photo', allow_empty_file=False)
    bio = forms.CharField(label='Bio', widget=forms.Textarea, required=True)
    dob = forms.DateField(label='Date of Birth', widget=DateInput(attrs={'type': 'date'}), required=True)