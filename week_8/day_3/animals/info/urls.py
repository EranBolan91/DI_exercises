from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('family/<id>',views.family,name='family'),
    path('animal/<id>',views.animal,name='animal'),
    path('people',views.people,name='people'),
    path('people/<id>',views.people_id,name='people'),
]