from django.urls import path
from . import views
from .views import *



urlpatterns = [
    path('homepage/', views.homepage, name='homepage'),
    path('add_film/', AddFilm.as_view(), name='add_film'),
    path('update_film/<int:pk>/', UpdateFilm.as_view(), name='update_film'),
    path('add_director/', AddDirector.as_view(), name='add_director'),
    path('update_director/<int:pk>/', UpdateDirector.as_view(), name='update_director'),
    path('delete_film/<int:pk>/', DeleteFilmView.as_view(), name='delete_film'),
    path('comment/<int:pk>',CommentViewForm.as_view(), name='comment'),
]