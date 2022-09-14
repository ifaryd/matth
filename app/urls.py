from django.urls import path
from .import views

urlpatterns = [

    path('', views.accueil, name='accueil'),
    path('accueil', views.accueil, name='accueil'),
    path('contacts', views.contacts, name='contacts'),
    path('predications-lists', views.predications_lists, name='predications-lists'),
    path('predications-details', views.predications_details, name='predications-details'),
    
]