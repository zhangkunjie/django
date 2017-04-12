from django import forms
class AddForm(forms.Form):
    name= forms.CharField()
    sex = forms.IntegerField()
    age= forms.IntegerField()
    email= forms.EmailField()
