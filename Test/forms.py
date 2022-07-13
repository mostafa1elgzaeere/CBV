from django.forms import *

class PlayerForm(Form):
    name=CharField(max_length=100)
    age=IntegerField()