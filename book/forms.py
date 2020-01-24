from django import forms
from .models import Book

class CreateForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["writer", "title", "date", "sub"]
    def __init__(self, *args, **kwargs):
        super(CreateForm, self).__init__(*args, **kwargs)
        self.fields["sub"].required=False
        
class FindForm(forms.Form):
    find = forms.CharField(label="Find", required=False)