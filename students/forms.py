from django import forms
from . models import student

class StudentForm(forms.ModelForm):
    class Meta:
        model = student
        fields = ['std_num','first_name','last_name','email','field_of_study','gpa']
        labels = {
            'std_num' : 'Student Number',
            'first_name' : 'First Name',
            'last_name' : 'Last Name',
            'email' : 'Email',
            'field_of_study' : 'Field of Study',
            'gpa' : 'GPA'
        }
        wigets = {
            'std_num': forms.NumberInput(attrs = {'class' : 'form-control'}),
            'first_name': forms.TextInput(attrs = {'class' : 'form-control'}),
            'last_name': forms.TextInput(attrs = {'class' : 'form-control'}),
            'email': forms.EmailInput(attrs = {'class' : 'form-control'}),
            'field_of_study': forms.TextInput(attrs = {'class' : 'form-control'}),
            'gpa': forms.NumberInput(attrs = {'class' : 'form-control'}),
        }
