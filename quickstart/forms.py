from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ContactForm(forms.Form):
    name = forms.CharField(required=True)
    surname = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    phone = forms.RegexField(regex=r'^\+?1?\d{9,15}$') # Only phone format allowed
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')

    # birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username','first_name', 'last_name','email','password1', 'password2', )