from django.contrib import admin
from .models import Formateur, Domaine, Secteur


@admin.register(Formateur)
class FormateurAdmin(admin.ModelAdmin):
    list_display = ('nom', 'domaines_display', 'secteurs_display', 'telephone', 'email', 'adresse', 'national')
    filter_horizontal = ('domaines', 'secteurs')
    search_fields = ('domaines__nom',)
    list_filter = ('domaines__nom',)


    def domaines_display(self, obj):
        return ', '.join(domaine.nom for domaine in obj.domaines.all())
    domaines_display.short_description = 'Domaines'

    def secteurs_display(self, obj):
        return ', '.join(str(secteur) for secteur in obj.secteurs.all())
    secteurs_display.short_description = 'Secteurs'

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == 'secteurs' and request.POST.get('national', False):
            kwargs['required'] = False
        return super().formfield_for_manytomany(db_field, request, **kwargs)
    

@admin.register(Secteur)
class SecteurAdmin(admin.ModelAdmin):
    model = Secteur
    ordering= ['code_postal']
# Enregistrer les autres modèles sans personnalisation

@admin.register(Domaine)
class DomaineAdmin(admin.ModelAdmin):
    model = Domaine
    ordering= ['nom']
