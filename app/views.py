from threading import local
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.utils.translation import ugettext as _

from . import models 

# Create your views here.


def accueil(request, lang):
    lang = lang
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
    predications= models.Predications.objects.filter(langue_id__initial=lang)
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

def predications_details(request, predications_id, lang):
    lang = lang
    currentpage = "predications-details/"+ str(predications_id)
    predications= models.Predications.objects.get(pk = int(predications_id))
    predications= models.Predications.objects.get(langue_id__initial = lang, numero = int(predications_id))
    versets =  models.Versets.objects.filter(predication_id__langue_id__initial=lang, predication_id__numero = int(predications_id))
   
    return render(request, 'predications-details.html', locals())

def presses_lists(request, lang):
    lang = lang
    return render(request, 'presses-lists.html')

def presses_details(request):
    return render(request, 'presses-details.html')