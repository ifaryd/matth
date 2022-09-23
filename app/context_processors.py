from app import models


def getlang(request):
    lang = models.Langues.objects.filter(initial__in = ['fr-fr', 'en-en', 'es-es', 'pt-pt'])
    data = {
        'langs':lang,
    }
    return data