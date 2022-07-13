from email import message
import re
from urllib import request
import django
from django.shortcuts import render
from django.views import View
from django.views.generic.list import ListView
from Test.forms import PlayerForm
from Test.models import Players
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
# Create your views here.

from django.views.generic.edit import CreateView , UpdateView , DeleteView
from django import forms



''' Django Forms '''
class AddPlayer(View):
    def get(self,request):
        form=PlayerForm()
        message=""
        return render(request,"Test\Players_form.html",{"form":form,"message":message})
    
    
    def post(self,request):
        message=""
        form=PlayerForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            age=form.cleaned_data['age']
            if Players.objects.filter(name=name).exists():
                message=""
                return render(request,"Test\Players_form.html",{"form":form,"message":message})

            else:    
                data=Players(name=name,age=age)
                data.save()
                form=PlayerForm()
                message="Add Succefly"
                
        return render(request,"Test\Players_form.html",{"form":form,"message":message})





























''' List View '''


# class PlayersListView(ListView):
#     model=Players
#     # context_object_name="Blala"
#     template_name="players_list.html"
    
#     def get_queryset(self):
#         return Players.objects.filter(pk=1)
    
#     def get_template_names(self):
#         if self.request.user.is_superuser:
#             template_name=""
#         elif self.request.user.is_authenticated:
#             template_name=""
#         else:
#             template_name=""         
#         return template_name
    

# def PlayerListView(request):
#     players_list=Players.objects.all()
#     return render(request,"players_list.html",{"players_list":players_list})

''' Detail View '''

# class PlayerDetail(DetailView):
#     model=Players
#     template_name="Test/player_detail.html"
    
    

# def PlayerDetail(request,pk):
#     player=Players.objects.get(id=pk)
#     return render(request,"player_deatil.html",{"player":player})     
    
    
    
    
''' Create View '''


# class CreatePlayer(CreateView):
#     model=Players
#     fields="__all__"
    
#     def get_form(self):
#         form =super().get_form()
#         form.fields["age"].widget=forms.PasswordInput(attrs={"class":"myclass"})
        
#         return form
        
''' Update View '''

# class UpdatePlayer(UpdateView):    
#     model=Players
#     fields="__all__"
#     template_name="Test/player_update.html"
#     # success_url=""




''' Delete View '''

# class DeletePlayer(DeleteView):
#     model=Players
#     success_url="/admin/"
    
    
    
    
    
    
    
    
    

''' Template View '''

# class PlayerTemplateView(TemplateView):
#     template_name="Test/players.html"
    
#     def get_context_data(self, **kwargs) :
#        context=super().get_context_data(**kwargs)
#        context['name']="mostafa"
#        return context
    
    