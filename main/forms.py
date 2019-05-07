from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, Form, fields

from main.models import School, Score

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
    
    def save(self, commit = True):
        sch = super(SchoolInfoForm, self).save(commit = False)
        sch.students_attending = 0
        sch.amount_paid = 0
        if commit:
            sch.save()
        return sch

class UpdateUserForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
    
class ScoringForm(ModelForm):
    class Meta:
        model = Score
        exclude = ()
        help_texts = {
            'documentation_score': 'Did student(s) include citations for sources and permissions for non-student produced materials?',
            'completion_score': 'Did student(s) complete the entire project?',
            'creativity_score':'Did student(s) use a higher level of creativity thoughout the design process and presentation?',
            'purpose_score':'Did all parts of the project work together for the intended purpose?',
            'understanding_score':'Did student(s) demonstrate a solid understanding of the software in development of the project?'
        }

    