from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name= 'home'),
    path('startexam/', views.startexam, name= 'startexam'),
    path('endexam/', views.endexam, name= 'endexam'),
    path('count/',views.count_quetion, name='count_quetion'),
]