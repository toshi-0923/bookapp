from django import forms
from .models import Day_sum
from django.forms import Textarea
from django.core.files.storage import default_storage

class CreateForm(forms.ModelForm):
    class Meta:
        model = Day_sum
        fields = ["date", "value"]
        #widgets = {
            #"value":Textarea(attrs={"cols":80, "rows":20}),
            #}
            
            
##アップロード場所
#class UploadForm(forms.Form):
#    file = forms.FileField(label="CSVファイル")
#    
#    def save(self):
#        upload_file = self.cleaned_data["file"]
#        file_name = default_storage.save(upload_file.name, upload_file)
#        return default_storage.url(file_name)