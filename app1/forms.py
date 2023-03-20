from django import forms

from app1.models import todo

class dateinput(forms.DateInput):
    input_type = 'date'

class timeinput(forms.TimeInput):
    input_type = 'time'


class todoform(forms.ModelForm):
    date=forms.DateField(widget=dateinput)
    time=forms.TimeField(widget=timeinput)
    class Meta:
        model = todo
        fields = '__all__'
