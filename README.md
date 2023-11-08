# Processus

## Versionning

La gestion des fichiers se fait sur GitHub : 
 - le front en React : https://github.com/SIGL-ESEO-E5A-G2/SIGL-frontend
 - le back en Python/Django : https://github.com/SIGL-ESEO-E5A-G2/SIGL-backend

## Realisation d'une US

1. Cloner le repos
2. Créer une branche pour l'US
3. Ajouter ses modifications
4. Créer un pull request pour fusionner l'US au projet
5. Faire valider son travail
6. Fusionner l'US

### Créer une branche

On considère qu'il y a trois type de branches : feature / refactor / lint .
- "feature" pour les branches dont le but est d'ajouter une nouvelle US / une nouvelle fonctionnalité.
- "refactor" pour les branches dont le but est de modifier une fonctionnalité déjà produite.
- "lint" pour les branches dont le but est d'apporter une correction.

Comment nommer une branche ? 

La branche doit commencer par le type de la branche [feat] ou [refac] ou [lint] suivi d'un '/'. Ensuite, un nom peut être choisi. Attention à choisir un nom qui permet de reconnaitre l'US associé, son numéro peut y être écrit.

exemple : feat/s3_deconnexion pour l'US SCRUM-3 [User] Deconnexion de la plateforme.

### Ecrire un commit

Le message d'un commit peut être important pour comprendre l'historique Git d'un projet. Je propose une écriture pour nos commit. 

exemple : "ajout(nomdufichier) : j'ai ajouter un fichier"

Le premier mot est un verbe qui décrit globalement le travail qui a été fait, entre parenthèse le fichier principal modifié puis une description du travail.

### Créer une pull request

Vous ne pourrez pas push directement sur la branche develop du projet car nous souhaitons quelle reste valide. Vous devrez créer une pull request que vous ferez valider par une personne du projet.

---
# Travailler avec le Backend
## Lancer le conteneur en local
Pour lancer la première fois conteneur, vous devez :
1. Allumer Docker (oui oui)
2. Se mettre à la racine du projet et lancer `docker-compose up --build`

Puis, pour seulement le lancer (sans build), vous pouvez executer `docker-compose up`

## Interagir avec le schéma de BD
Pour intéragir avec la BD, on utilise l'ORM de Django.
### Créer une table
Pour créer une table :
1. Créer un modèle dans `api/models.py`.
2. Aller dans le terminal du conteneur sigl-backend (soit en ligne de commande soit par l'interface de Docker).
3. Se mettre à la racine du projet et executer `python manage.py makemigrations api`.
4. Se mettre à la racine du projet et executer `python manage.py migrate`.

### Modifier une table
Pour Modifier une table :
1. Modifier la table voulue (ajoute d'une colonne par exemple) dans `api/models.py`.
2. Aller dans le terminal du conteneur sigl-backend (soit en ligne de commande soit par l'interface de Docker).
3. Se mettre à la racine du projet et executer `python manage.py makemigrations api`.
4. Se mettre à la racine du projet et executer `python manage.py migrate`.

### Remplir une table avec des données de test
Pour créer des données de test (fixtures) :
1. Créer un fichier {model}_fixtures.json
2. Remplir les données en fonctions des champs du modèle, exemple avec Utilisateur :
```json
    [
    {
        "model": "api.utilisateur",
        "pk": 1,
        "fields": {
            "nom": "ALLORY",
            "prenom": "Corantin",
            "email": "corantin.allory@reseau.eseo.fr",
            "motDePasse": "MotDePasseAleatoire1",
            "roles":[1]
        }
    },
    ...
    ]
```
3. Aller dans le terminal du conteneur sigl-backend (soit en ligne de commande soit par l'interface de Docker).
4. Se mettre à la racine du projet et executer `python ./manage.py loaddata {model}_fixtures.json`.