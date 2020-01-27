from django import forms
from .models import Day_sum
from django.forms import Textarea

class CreateForm(forms.ModelForm):
    class Meta:
        model = Day_sum
        fields = ["date", "value"]

#widgets = {
#"value":Textarea(attrs={"cols":80, "rows":20}),
#}