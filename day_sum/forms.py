from django import forms
from .models import Day_sum

class CreateForm(forms.ModelForm):
    class Meta:
        model = Day_sum
        fields = ["date", "value"]
        