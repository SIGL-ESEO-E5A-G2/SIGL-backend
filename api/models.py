from django.db import models

# =================== EXEMPLE =======================
# class Species(models.Model):
#    name = models.CharField(max_length=100)
#    classification = models.CharField(max_length=100)
#    language = models.CharField(max_length=100)
#    planet = models.CharField(max_length=100)

class SemestreEnum(models.TextChoices):
    S5 = 'S5', 'S5'
    S6 = 'S6', 'S6'
    S7 = 'S7', 'S7'
    S8 = 'S8', 'S8'
    S9 = 'S9', 'S9'
    S10 = 'S10', 'S10'

class RoleEnum(models.TextChoices):
   Apprenti = 'Apprenti', 'Apprenti'
   TuteurPedagogique = 'TuteurPedagogique', 'TuteurPedagogique'
   Administrateur = 'Administrateur', 'Administrateur'
   CoordinatriceAlternance = 'CoordinatriceAlternance', 'CoordinatriceAlternance'
   MaitreAlternance = 'MaitreAlternance', 'MaitreAlternance'

class Role(models.Model):
   id = models.AutoField(primary_key=True)
   libelle = models.CharField(max_length=25, choices= RoleEnum.choices, default=RoleEnum.Apprenti)

class Utilisateur(models.Model):
   id = models.AutoField(primary_key=True)
   nom = models.CharField(max_length=255)
   prenom = models.CharField(max_length=255)
   email = models.CharField(max_length=255)
   motDePasse = models.CharField(max_length=255)
   roles = models.ManyToManyField(Role)

class Administrateur(models.Model):
   id = models.AutoField(primary_key=True)
   idUtilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)

class TuteurPedagogique(models.Model):
   id = models.AutoField(primary_key=True)
   idUtilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)

class CoordinatriceAlternance(models.Model):
   id = models.AutoField(primary_key=True)
   idUtilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)

class MaitreAlternance(models.Model):
   id = models.AutoField(primary_key=True)
   idUtilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
   entreprise = models.CharField(max_length=255)

class Promotion(models.Model):
   id = models.AutoField(primary_key=True)
   libelle = models.CharField(max_length=255)
   semestre = models.CharField( max_length=3, choices=SemestreEnum.choices, default=SemestreEnum.S5)

class Apprenti(models.Model):
   id = models.AutoField(primary_key=True)
   idUtilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
   idTuteurPedagogique = models.ForeignKey(TuteurPedagogique, on_delete=models.CASCADE)
   idMaitreAlternance = models.ForeignKey(MaitreAlternance, on_delete=models.CASCADE)
   optionMajeure = models.CharField(max_length=255)
   optionMineure = models.CharField(max_length=255)