from typing import Any
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

    
class RegisterForm(UserCreationForm): # Registration form Setting fields and details
    email = forms.EmailField(max_length= 254, help_text='Required. Add a valid email address.')
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
    
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self ).__init__(*args, **kwargs)
        
        for fieldname in ['username','password1','password2']: # Loop through the fields and remove the help text
            self.fields[fieldname].help_text = None