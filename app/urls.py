
from django.urls import path
from  .import views


urlpatterns = [
    
    path('',views.homee,name='home')
]
