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