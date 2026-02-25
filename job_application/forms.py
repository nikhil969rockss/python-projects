from django import forms

class ApplicationForm(forms.Form):
    first_name = forms.CharField(max_length=80,required=True )
    last_name = forms.CharField(max_length=80, required=True )
    email = forms.EmailField(max_length=100,required=True )
    date = forms.DateField()
    occupation = forms.CharField(max_length=20,)
