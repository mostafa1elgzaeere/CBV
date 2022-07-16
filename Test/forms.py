from turtle import mode
from django.forms import *

from Test.models import Players

''' Django ModelForm'''
class PlayerForm(ModelForm):
    class Meta:
        model=Players
        fields="__all__"
        
        help_text={
            'name':'Enter Your Name',
            'age':"Enter Your Age"
        }
        
        error_messages={
            'name':{'requierd':"Enter right Name"}
        }
        
        


















''' Django Forms'''
# class PlayerForm(Form):
#     name=CharField(max_length=100)
#     age=IntegerField()
    
#     def clean(self):
#         cleaned_data=super().clean()
#         validated_name=self.cleaned_data['name']
        
#         if Players.objects.filter(name=validated_name).exists():
#             raise ValidationError("user already exists")
        
        