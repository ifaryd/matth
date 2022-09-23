from django.urls import path
from .import views

urlpatterns = [

    #---- langue
    path('<slug:lang>/', views.index, name='index'),
    path('', views.accueil, name='accueil'),
    path('<slug:lang>/accueil', views.accueil, name='accueil'),
    path('<slug:lang>/contacts', views.contacts, name='contacts'),
    path('<slug:lang>/predications-lists', views.predications_lists, name='predications-lists'),
    path('<slug:lang>/predications-details/<int:predications_id>', views.predications_details, name='predications-details'),
    path('<slug:lang>/presses-lists', views.presses_lists, name='presses-lists'),
    path('<slug:lang>/presses-details', views.presses_details, name='presses-details'),

    
    
]