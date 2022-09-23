from django.contrib import admin


from . import models


class LanguesAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'initial',
        
    )
    ordering = ['id']
    list_filter = (
        'initial',
    )

class PredicationsAdmin(admin.ModelAdmin):

    list_display = ('numero','chapitre','titre','duree','langue_id',)
    ordering = ['id']
    list_filter = ('langue_id',)
    search_fields = ['numero','titre','langue_id',]
    list_display_links = ['numero', 'titre', 'chapitre',]
    

class VersetsAdmin(admin.ModelAdmin):

    list_display = ('predication_id','numero',)
    list_filter = []
    ordering = ['numero']
    list_per_page = 100
    search_fields = ['numero']
    list_display_links = ['numero', 'predication_id',]




def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Langues, LanguesAdmin)   
_register(models.Predications, PredicationsAdmin)   
_register(models.Versets, VersetsAdmin)