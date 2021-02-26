from django import forms
from .models import member



class memberform(forms.ModelForm):

    class Meta:

       model = member
     #it will take the fields from the models
       fields = ['fname','lname','age','password','email','birthdate']
