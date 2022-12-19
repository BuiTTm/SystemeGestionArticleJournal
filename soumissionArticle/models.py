from django.db import models
from django.conf import settings


class Article(models.Model):
    class Categorie(models.TextChoices):
        ARCHITECTURE = 'AR', 'Architecture'
        ARTIFICIAL_INTELLIGENCE = 'AI', 'Artificial Intelligence'
        BIOINFORMATICS = 'BI', 'Bioinformatics'
        BIOMEDICAL_ENGINEERING = 'BE', 'Biomedical Engineering'
        BIOTECHNOLOGY = 'BT', 'Biotechnology'
        COMPUTER_SOFTWARE_AND_APPLICATIONS = 'CS', 'Computer software and applications'
        COMPUTING = 'CO', 'Computing'
        ENGINEERING = 'EG', 'Engineering'
        IMAGE_PROCESSING = 'IP', 'Image Processing'
        INFORMATION_TECHNOLOGY = 'IT', 'Information Technology'
        INTERNET_AND_WORLD_WIDE_WEB = 'IN', 'Internet and World Wide Web'
        MANUFACTURING = 'MA', 'Manufacturing'
        NANOTECHNOLOGY_AND_SMART_MATERIALS = 'NT', 'Nanotechnology and Smart Materials'
        POLYMERS_AND_PLASTICS = 'PP', 'Polymers and Plastics'
        RENEWABLE_GREEN_ENERGY = 'RG', 'Renewable & Green Energy'
        ROBOTICS = 'RB', 'Robotics'
        SPACE_ENVIRONMENT_AND_AVIATION_TECHNOLOGY = 'SA', 'Space Environment and Aviation Technology'
        SYSTEMS_ENGINEERING = 'SE', 'Systems Engineering'

    class Statut(models.TextChoices):
        EN_ATTENTE = "0", "En attente"
        REFUSE_AVEC_COMMENTAIRES = "1", "Refusé avec commentaires"
        ACCEPTE_AVEC_COMMENTAIRES_MINEURS = "2", "Accepté avec commentaires mineurs"
        ACCEPTE_AVEC_COMMENTAIRES_MAJEURS = "3", "Accepté avec commentaires majeurs"
        ACCEPTE_SANS_COMMENTAIRE = "4", "Accepté sans commentaire"

    categorie = models.CharField(max_length=2, choices=Categorie.choices, default=Categorie.ARCHITECTURE)
    statut = models.CharField(max_length=2, choices=Statut.choices, default=Statut.EN_ATTENTE)
    titre = models.TextField(blank=False)
    description = models.TextField(blank=False, default='')
    auteurs_secondaires = models.TextField(blank=False, default='')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    auteur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, editable=False, blank=False)


class SoumissionArticle(models.Model):
    titre = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre
