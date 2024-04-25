from django.forms import ModelForm
from django import forms
from .models import Organization, OrgMember, Student, College, Program

class OrganizationForm(ModelForm):
    class Meta:
        model = Organization
        fields = "__all__"

class OrgMemberForm(ModelForm):
    date_joined = forms.DateField(label="Date joined",
                                 widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    class Meta:
        model = OrgMember
        fields = "__all__"

class StudentForm(ModelForm):
    birth_date = forms.DateField(label="Birthdate",
                                 widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    class Meta:
        model = Student
        fields = "__all__"

class CollegeForm(ModelForm):
    class Meta:
        model = College
        fields = "__all__"

class ProgramForm(ModelForm):
    
    class Meta:
        model = Program
        fields = "__all__"