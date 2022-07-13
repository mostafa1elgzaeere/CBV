from django.forms import *

from Test.models import Players

class PlayerForm(Form):
    name=CharField(max_length=100)
    age=IntegerField()
    
    def clean(self):
        cleaned_data=super().clean()
        validated_name=self.cleaned_data['name']
        
        if Players.objects.filter(name=validated_name).exists():
            raise ValidationError("user already exists")
        