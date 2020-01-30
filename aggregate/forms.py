from django import forms
from django.core.files.storage import default_storage

            
##アップロード場所
class UploadForm(forms.Form):
    file = forms.FileField(label="CSVファイル")
