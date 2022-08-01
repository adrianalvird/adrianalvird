from django import forms

class UploadFileForm(forms.Form):
    name = forms.CharField(max_length=50)
    priemail = forms.CharField(max_length=100)
    extemail = forms.CharField(max_length=100)
    jobdesc = forms.CharField(max_length=50)
    resume = forms.FileField()
    date = forms.CharField(max_length=50)
    photo = forms.FileField()
    phone = forms.CharField(max_length=50)
    country = forms.CharField(max_length=50)
    address = forms.CharField(max_length=200)
    message = forms.CharField(max_length=200)

