from .models import home
from django.shortcuts import render


# Create your views here.

 


def homee(request):

    u = home.objects.filter(place = 'sanand') 
    return render(request,'app/home.html',{'u':u})


# class lol():

#   def get_queryset(self):
#      user = self.request.user
#      return home.objects.filter(place = user) 
