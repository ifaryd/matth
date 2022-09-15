from django.shortcuts import render

# Create your views here.


def accueil(request):
    return render(request, 'index.html')

def contacts(request):
    return render(request, 'contacts.html')

def predications_lists(request):
    return render(request, 'predications-lists.html')

def predications_details(request):
    return render(request, 'predications-details.html')

def presses_lists(request):
    return render(request, 'presses-lists.html')

def presses_details(request):
    return render(request, 'presses-details.html')