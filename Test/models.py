from unicodedata import name
from django.db.models import *
from django.urls import reverse 

# Create your models here.


class Players(Model):
    name=CharField(max_length=100)
    age=IntegerField()
    
    def __str__(self) :
        return self.name
    
    # def get_absolute_url(self):
    #     return reverse("player_detail", kwargs={"pk": self.pk})
    