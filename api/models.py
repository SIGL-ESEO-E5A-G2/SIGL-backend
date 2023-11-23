from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from datetime import date, datetime

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

class UtilisateurManager(BaseUserManager):
    def create_user(self, email, nom, prenom, mot_de_passe=None, **extra_fields):
        if not email:
            raise ValueError('L\'adresse e-mail doit être définie')
        email = self.normalize_email(email)
        utilisateur = self.model(email=email, nom=nom, prenom=prenom, **extra_fields)
        utilisateur.set_password(mot_de_passe)
        utilisateur.save(using=self._db)
        return utilisateur

    def create_superuser(self, email, nom, prenom, mot_de_passe=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, nom, prenom, mot_de_passe, **extra_fields)

class Utilisateur(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    roles = models.ManyToManyField(Role)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UtilisateurManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nom', 'prenom']

class Administrateur(models.Model):
   id = models.AutoField(primary_key=True)
   utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)

class TuteurPedagogique(models.Model):
   id = models.AutoField(primary_key=True)
   utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)

class CoordinatriceAlternance(models.Model):
   id = models.AutoField(primary_key=True)
   utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)

class MaitreAlternance(models.Model):
   id = models.AutoField(primary_key=True)
   utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)

class Promotion(models.Model):
   id = models.AutoField(primary_key=True)
   libelle = models.CharField(max_length=255)
   semestre = models.CharField( max_length=3, choices=SemestreEnum.choices, default=SemestreEnum.S5)

class Apprenti(models.Model):
   id = models.AutoField(primary_key=True)
   utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
   tuteurPedagogique = models.ForeignKey(TuteurPedagogique, on_delete=models.CASCADE)
   maitreAlternance = models.ForeignKey(MaitreAlternance, on_delete=models.CASCADE)
   optionMajeure = models.CharField(max_length=255, default="N/A")
   optionMineure = models.CharField(max_length=255, default="N/A")


class Message(models.Model):
    id = models.AutoField(primary_key=True)
    titre = models.TextField()
    contenu = models.TextField()
    date = models.DateField(default = date.today)
    time = models.TimeField(default = datetime.now())
    createur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='createur_message')
    destinataire = models.ManyToManyField(Utilisateur)

class Depot(models.Model):
    id = models.AutoField(primary_key=True)
    message = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    echeance = models.DateField(default=date.today)
    chemin_fichier = models.CharField(max_length=255)