from logging import Filter
from re import L
from threading import local
from django.http import request
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.utils.translation import ugettext as _
import requests

import json
import time
from . import models

# Create your viewsc here.


def accueil(request, lang):
    lang = lang
    return redirect('/fr-fr/')

def start(request):
    return redirect('/fr-fr/')

def index(request, lang):
    lang = lang
    currentpage = ""
    return render(request, 'index.html')

def galeries(request, lang):
    lang = lang
    photos= models.Photos.objects.all()
    return render(request, 'galeries.html', locals())

def videos(request, lang):
    lang = lang
    videos = models.Videos.objects.all()[:4]
    return render(request, 'predications-videos.html', locals())

def contacts(request, lang):
    lang = lang
    return render(request, 'contacts.html')


    
   



def predications_lists(request, lang):
    lang = lang

    langue=requests.get("https://api.philippekacou.site/api/langues/"+lang)
    langue_id=1
    if langue:
        langue_id=langue.json()['id']
    url1= "https://api.philippekacou.site/api/predications?langue="+ str(langue_id)
    response=requests.get(url1)
    predications=response.json()['data']

    # predications = [x for x in predication if x["langue"]["initial"] == lang]
  
  

    paginator = Paginator(predications, 50)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        predications = paginator.page(page)
    except(EmptyPage, InvalidPage):
        predications = paginator.page(paginator.num_pages)
    return render(request, 'predications-lists.html', locals())


# currentpage = "predications-details/"+ str(predications_id)
#     predications= models.Predications.objects.get(pk = int(predications_id))
#     predications= models.Predications.objects.get(langue_id__initial = lang, numero = int(predications_id))
#     versets =  models.Versets.objects.filter(predication_id__langue_id__initial=lang, predication_id__numero = int(predications_id))

def predications_details(request, predications_id, lang):
    lang = lang

    url1= "https://api.philippekacou.site/api/versets?predication=" + str(predications_id)
    response=requests.get(url1)
    versets=response.json()['data']

    url2= "https://api.philippekacou.site/api/predications/" + str(predications_id)
    response2=requests.get(url2)
    predications=response2.json()

    data={
        'versets':versets,
        'predications':predications,
    }
    # predications = [x for x in predication if x["langue"]["id"] == predications_id]

    # with open('predications_list.json', 'r') as openfile:
    #     predication = json.load(openfile)
    # predications = [x for x in predication if x["langue"]["initial"] == lang]


    # with open('versets_list.json', 'r') as openfile:
    #     verset = json.load(openfile)
    # versets = [x for x in verset if x["langue_id"] == lang]
    
    return render(request, 'predications-details.html', data)

def presses_lists(request, lang):
    lang = lang
    return render(request, 'presses-lists.html')

def presses_details(request):
    return render(request, 'presses-details.html')