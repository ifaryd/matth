
import requests
import json
from app import models

# def recup_pred():
#     response = requests.get('https://api.philippekacou.site/api/langues') # (your url)
#     langs = response.json()['data']
#     with open('langues.json', 'w') as f:
#         json.dump(langs, f)

# def getlang(request):
#     lang = models.Langues.objects.filter(initial__in = ['fr-fr', 'en-en', 'es-es', 'pt-pt'])
#     data = {
#         'langs':lang,
#     }
#     return data

# def recup_lang():
#     response = requests.get('https://api.philippekacou.site/api/langues') # (your url)
#     langue = response.json()['data']
#     with open('langues_list.json', 'w') as f:
#         json.dump(langue, f)
#     print("jegbizejbzejvbdnkv,zbdvhzdjnvbz")

# def getlang():
#     with open('langues_list.json', 'r') as openfile:
#         langue = json.load(openfile)

# def getlang(request):
#     with open('langues.json', 'r') as openfile:
#         lang = json.load(openfile)
#         print(lang)
#     data = {
#         'langs':lang,
#     }

#     return data


   


    # url= "https://api.philippekacou.site/api/predications"
    # response=requests.get(url)
    # data=response.json()["data"][:4]
    # return render(request, 'api.html', {'data':data})

    # models.Langues.objects.filter(initial__in = ['fr-fr', 'en-en', 'es-es', 'pt-pt'])



def getlang(request):
    url= "https://api.philippekacou.site/api/langues"
    response=requests.get(url)
    lang = response.json()["data"]
    data = {
        'langs':lang,
    }
    return data