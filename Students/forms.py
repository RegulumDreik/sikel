from django import forms
from .models import StudentModel


class StudentForm(forms.ModelForm):
    class Meta:
        model=StudentModel
        fields=['first_name', 'middle_name', 'last_name', 'date_of_birth']