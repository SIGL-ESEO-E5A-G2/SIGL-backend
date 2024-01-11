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
    telephone = models.CharField(max_length=255)
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

class Entreprise(models.Model):
   id = models.AutoField(primary_key=True)
   raisonSociale = models.CharField(max_length=255, default="N/A")
   adresse = models.CharField(max_length=255, default="N/A")
   secteurDactivite = models.CharField(max_length=255, default="N/A")
   description = models.TextField(default="N/A")
   siret = models.CharField(max_length=255, default="N/A")
   libelleCPNE = models.CharField(max_length=255, default="N/A")
   codeIDCC = models.CharField(max_length=255, default="N/A")
   conventionCollective = models.CharField(max_length=255, default="N/A")
   codeNAF = models.CharField(max_length=255, default="N/A")
   telephone = models.CharField(max_length=255, default="N/A")
   email = models.CharField(max_length=255, default="N/A")
   nombreSalarie = models.IntegerField(default=0)

class ResponsableEntreprise(models.Model):
   id = models.AutoField(primary_key=True)
   nom = models.CharField(max_length=255)
   prenom = models.CharField(max_length=255)
   telephone = models.CharField(max_length=255)
   email = models.CharField(max_length=255)
   fonction = models.CharField(max_length=255)
   ancienEseo = models.BooleanField(default=False)
   entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE)

class Opco(models.Model):
   id = models.AutoField(primary_key=True)
   raisonSociale = models.CharField(max_length=255, default="N/A")
   adresse = models.CharField(max_length=255, default="N/A")
   siret = models.CharField(max_length=255, default="N/A")
   telephone = models.CharField(max_length=255, default="N/A")
   email = models.CharField(max_length=255, default="N/A")

class MaitreAlternance(models.Model):
   id = models.AutoField(primary_key=True)
   utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
   fonction = models.CharField(max_length=255, default="N/A")
   dernierDiplome = models.CharField(max_length=255, default="N/A")
   ancienEseo = models.BooleanField(default=False)
   entreprise = models.ForeignKey(Entreprise, blank=True, null=True, on_delete= models.SET_NULL)

class Promotion(models.Model):
   id = models.AutoField(primary_key=True)
   libelle = models.CharField(max_length=255)
   semestre = models.CharField( max_length=3, choices=SemestreEnum.choices, default=SemestreEnum.S5)

class GrilleEvaluation(models.Model):
   id = models.AutoField(primary_key=True)
   
class Competence(models.Model):
   id = models.AutoField(primary_key=True)
   libelle = models.CharField(max_length=255)
   description = models.TextField(default="N/A")
   
class EtatEvaluationEnum(models.TextChoices):
    NON_ACQUIS = 'Non acquis', 'Non acquis'
    EN_COURS = 'En cours d\'acquisition', 'En cours d\'acquisition'
    ACQUIS = 'Acquis', 'Acquis'
    NON_ABORDE = 'Non abordé en entreprise', 'Non abordé en entreprise'   
    
class CompetenceApprenti(models.Model):
   id = models.AutoField(primary_key=True)
   commentaire = models.CharField(max_length=255, default="N/A")
   competence = models.ForeignKey(Competence, blank=True, null=True, on_delete= models.CASCADE)
   grilleEvaluation = models.ForeignKey(GrilleEvaluation, blank=True, null=True, on_delete= models.CASCADE)
   semestre = models.CharField( max_length=3, choices=SemestreEnum.choices, default=SemestreEnum.S5)
   evaluation = models.CharField( max_length=24, choices=EtatEvaluationEnum.choices, default=EtatEvaluationEnum.NON_ACQUIS)
   cible = models.CharField( max_length=24, choices=EtatEvaluationEnum.choices, default=EtatEvaluationEnum.NON_ACQUIS)

   
class Apprenti(models.Model):
   id = models.AutoField(primary_key=True)
   utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
   tuteurPedagogique = models.ForeignKey(TuteurPedagogique,  blank=True, null=True, on_delete= models.SET_NULL)
   maitreAlternance = models.ForeignKey(MaitreAlternance,  blank=True, null=True, on_delete= models.SET_NULL)
   optionMajeure = models.CharField(max_length=255, default="N/A")
   optionMineure = models.CharField(max_length=255, default="N/A")
   promotion = models.ForeignKey(Promotion, blank=True, null=True, on_delete= models.SET_NULL)
   intitulePoste = models.CharField(max_length=255, default="N/A")
   descriptifPoste = models.TextField(default="N/A")
   classificationConventionCollective = models.CharField(max_length=255, default="N/A")
   dureeHebdoContrat = models.IntegerField(default=35)
   entreprise = models.ForeignKey(Entreprise, blank=True, null=True, on_delete= models.SET_NULL)
   opco = models.ForeignKey(Opco, blank=True, null=True, on_delete= models.SET_NULL)
   grilleEvaluation = models.ForeignKey(GrilleEvaluation, blank=True, null=True, on_delete= models.SET_NULL)

class TypeTagEnum(models.TextChoices):
    LIVRABLE = 'Livrable', 'Livrable'
    NOTE = 'Note', 'Note'
    AUTRE = 'Autre', 'Autre'

class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    libelle = models.CharField(max_length=255, default="N/A")
    type = models.CharField(max_length=10, choices=TypeTagEnum.choices, default=TypeTagEnum.AUTRE)

class Message(models.Model):
    id = models.AutoField(primary_key=True)
    titre = models.CharField(max_length=255,default="N/A")
    contenu = models.TextField(default="N/A")
    date = models.DateField(default = date.today)
    time = models.TimeField(default = datetime.now())
    createur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='createur_message')
    destinataire = models.ManyToManyField(Utilisateur)
    tags = models.ManyToManyField(Tag)

class Depot(models.Model):
    id = models.AutoField(primary_key=True)
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    echeance = models.DateField(default=date.today)
    cheminFichier = models.CharField(max_length=255)

class Evenement(models.Model):
    id = models.AutoField(primary_key=True)
    libelle =models.CharField(max_length=255 , default="N/A")
    dateDebut = models.DateField(default=date.today)
    dateFin = models.DateField(default=date.today)
    description = models.TextField(default="N/A")
    apprenti = models.ForeignKey(Apprenti, on_delete=models.CASCADE)

class EntretienSemestriel(models.Model):
   id = models.AutoField(primary_key=True)
   evenement = models.ForeignKey(Evenement, on_delete=models.CASCADE)
   tuteurPedagogique = models.ForeignKey(TuteurPedagogique, blank=True, null=True, on_delete= models.SET_NULL)
   maitreAlternance = models.ForeignKey(MaitreAlternance, blank=True, null=True, on_delete= models.SET_NULL)
   noteSemestre = models.IntegerField(default=-1)
   
class Commentaire(models.Model):
   id = models.AutoField(primary_key=True)
   contenu = models.TextField(default="N/A")
   date = models.DateField(default = date.today)
   time = models.TimeField(default = datetime.now())
   createur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='createur_commentaire')
   message = models.ForeignKey(Message, on_delete=models.CASCADE)

   
