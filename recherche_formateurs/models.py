from django.db import models

class Domaine(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

class Secteur(models.Model):
    nom = models.CharField(max_length=100)
    code_postal = models.CharField(max_length=5, null=True, blank=True)

    class Meta:
        ordering = ['code_postal']

    def __str__(self):
        return f"{self.nom} ({self.code_postal})"

class Formateur(models.Model):
    nom = models.CharField(max_length=100)
    domaines = models.ManyToManyField(Domaine, related_name='formateurs')
    secteurs = models.ManyToManyField(Secteur, related_name='formateurs')
    telephone = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    adresse = models.TextField(blank=True, null=True)
    commentaires = models.TextField(blank=True, null=True)
    national = models.BooleanField(default=False)


    def __str__(self):
        return self.nom