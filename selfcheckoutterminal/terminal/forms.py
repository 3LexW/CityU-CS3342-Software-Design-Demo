from django import forms
import datetime

class BirthdayForm(forms.Form):
    birthday = forms.DateField(
        label = '', 
        widget=forms.SelectDateWidget(
            years=range(1900, datetime.datetime.today().year + 1)),
        initial = datetime.datetime.now(),
    )