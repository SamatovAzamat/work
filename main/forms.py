from django import forms
from django.core.validators import EmailValidator, RegexValidator
from django.core.exceptions import ValidationError
from .models import Post



class PostForm(forms.ModelForm):
    class Meta:
        model =Post
        fields = ['category', 'subject_uz', 'subject_ru', 'content_uz', 'content_ru', 'image']


# class IsmForm(forms.Form):
#     ism = forms.CharField(max_length=100)
#     fam = forms.CharField(max_length=100)
#     ty = forms.IntegerField(min_value=1900, widget=forms.TextInput)
#     email = forms.EmailField()