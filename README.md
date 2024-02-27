[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
# Projet Prime GPT (Flask)

Cette application a été conçue pour la société Prime Engineering afin qu'ils puissent l'utiliser dans leur processus de recrutement.
Elle réalise un résumé de CV en quelques lignes à l'aide de l'API de ChatGPT et selon 2 formats standards de résumés.

## Pré-requis

* Installer Python 3 : [Téléchargement Python 3](https://www.python.org/downloads/)
* Installer git : [Téléchargement Git](https://git-scm.com/book/fr/v2/D%C3%A9marrage-rapide-Installation-de-Git)

## Installation

### 1. Télécharger le projet sur votre répertoire local : 
```
git clone  
cd 
```
### 2. Mettre en place un environnement virtuel :
* Créer l'environnement virtuel: `python -m venv venv`
* Activer l'environnement virtuel :
    * Windows : `venv\Scripts\activate.bat`
    * Unix/MacOS : `source venv/bin/activate`

    
### 3. Installer les dépendances du projet
```
pip install -r requirements.txt
```

## 4. Renseigner clé API Chat GPT

Renseigner une clé API Chat GPT associé à votre compte Open AI dans le fichier .env

## Démarrage
* Lancer le script à l'aide de la commande suivante : `flask run`

## Tests

* Lancer les tests à l'aide de la commande suivante : `pytest`