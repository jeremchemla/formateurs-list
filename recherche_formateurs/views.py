from django.db.models import Q
from .models import Formateur
from django.shortcuts import render

def search_formateurs(request):
    nom = request.GET.get('nom', '')
    domaines = request.GET.get('domaines', '').split()
    secteur = request.GET.get('secteur', '')
    national = request.GET.get('national', True)

    formateurs = Formateur.objects.all()

    # Filtrer par nom/prénom
    if nom:
        formateurs = formateurs.filter(nom__icontains=nom).distinct()

    # Filtrer par domaines
    if domaines:
        domaines_query = Q()
        for domaine in domaines:
            domaines_query |= Q(domaines__nom__icontains=domaine)
        formateurs = formateurs.filter(domaines__nom__icontains=domaine).distinct()

    # Filtrer par secteur ou code postal
    secteur_query = Q(secteurs__nom__icontains=secteur) | Q(secteurs__code_postal__icontains=secteur)
    if not national:
        formateurs = formateurs.filter(secteur_query).distinct()
    else:
        formateurs = formateurs.filter(Q(secteur_query) | Q(national=True)).distinct()
    


    # Si la case "national" est cochée, inclure les formateurs nationaux


    context = {
        'formateurs': formateurs,
        'nom': nom,
        'domaines': ' '.join(domaines),
        'secteur': secteur,
        'national': national,
    }
    return render(request, 'app/search_formateurs.html', context)