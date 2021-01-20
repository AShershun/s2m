from django import forms
from app.models import Degree, Department, Faculty, Institute, Post, Rank, Scientist, Speciality


class SelectForm(forms.ModelForm):
    class Meta:
        model = Scientist
        fields = [
            'lastname_uk',
            'firstname_uk',
        ]
