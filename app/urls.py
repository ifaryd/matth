from django.urls import path
from .import views

urlpatterns = [
   
    #---- accueil
    path('', views.start, name='start'),
    path('<slug:lang>/', views.index, name='index'),
    path('<slug:lang>/accueil', views.accueil, name='accueil'),
    path('<slug:lang>/predications-details/accueil', views.accueil, name='accueil'),

     #---- galeries
    path('<slug:lang>/galeries', views.galeries, name='galeries'),
    path('<slug:lang>/predications-details/galeries', views.galeries, name='galeries'),

#---- predications
    path('<slug:lang>/predications-details/predications-lists', views.predications_lists, name='predications-lists'),
    path('<slug:lang>/predications-lists', views.predications_lists, name='predications-lists'),
    path('<slug:lang>/predications-details/<int:predications_id>', views.predications_details, name='predications-details'),
    path('<slug:lang>/predications-videos', views.videos, name='predications-videos'),
    path('<slug:lang>/predications-details/predications-videos', views.videos, name='predications-videos'),

#---- contacts
    path('<slug:lang>/contacts', views.contacts, name='contacts'),
    path('<slug:lang>/predications-details/contacts', views.contacts, name='contacts'),

#---- presses
    path('<slug:lang>/presses-lists', views.presses_lists, name='presses-lists'),
    path('<slug:lang>/presses-details', views.presses_details, name='presses-details'),

    
    
]