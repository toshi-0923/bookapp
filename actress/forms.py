from django import forms
from .models import Actress
            
##アップロード場所
class CreateForm(forms.ModelForm):
    class Meta:
        model = Actress
        fields = \
        ["image","no","name","age","visit","work","hobby","birth","co_date","date","memo","scenario"]
