from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, Form, fields

from main.models import School

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit = False)
        user.email = self.cleaned_data["email"]

        if commit:
            user.save()
        return user

class SchoolInfoForm(ModelForm):

    def __init__(self, **kwargs):
        self.contact_email = kwargs.pop('email')
        super(SchoolInfoForm, self).__init__( **kwargs)
        if not self.instance:
            self.fields['email'].initial = self.contact_email


    contact_alternate_phone = forms.CharField(max_length=64, required=False)
    contact_email = forms.CharField(max_length = 192)
    class Meta:
        model = School
        
        fields = [
            "school_name", 
            "address", 
            "contact_name",
            "contact_email", 
            "contact_primary_phone", 
            "contact_alternate_phone", 
            "chaperones_attending", 
            "teachers_attending", 
            "drivers_attending"
            ]