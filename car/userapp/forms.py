# userapp/forms.py
from django import forms
from .models import *

class usersignupform(forms.ModelForm):
    class Meta:
        model = usersignup
        fields = "__all__"



class usercontactform(forms.ModelForm):
    class Meta:
        model = usercontact
        fields = "__all__"


class bookserviceform(forms.ModelForm):
    class Meta:
        model = bookservice
        fields = ["name","phone","service","date","specialrequest"]