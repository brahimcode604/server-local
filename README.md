#  Serveur Local d'Upload d'Images

Un projet de serveur local léger, sécurisé et optimisé pour le téléchargement (upload) et l'affichage d'images, conçu avec **Python (Flask)** pour le backend et **HTML/JavaScript** pour le frontend.

![Repository](https://img.shields.io/badge/GitHub-Repository-blue?logo=github&style=flat-square) 
[Accéder au dépôt GitHub](https://github.com/brahimcode604/server-local.git)

---

##  Fonctionnalités

- **Upload Sécurisé** : Validation stricte des extensions de fichiers (`png`, `jpg`, `jpeg`, `gif`, `webp`) et sécurisation des noms de fichiers.
- **Optimisation du Stockage** : Renommage automatique des images avec des **UUID** (Identifiants Uniques Universels) pour éviter les collisions et masquer les métadonnées originales.
- **Protection Anti-DDoS/Surcharge** : Limite de taille imposée pour les fichiers uploadés (5 Mo maximum).
- **Galerie Dynamique** : Une interface frontend simple `index.html` permettant de téléverser des images et de les afficher instantanément via des appels API asynchrones.
- **Sécurité CORS** : L'API restreint l'accès aux origines autorisées pour protéger les endpoints.

---

##  Technologies Utilisées

- **Backend** :  Python, Flask, Flask-CORS, Werkzeug
- **Frontend** :  HTML5, CSS3, JavaScript (Fetch API)

---

##  Installation & Démarrage

### 1. Cloner le projet
```bash
git clone https://github.com/brahimcode604/server-local.git
cd server-local
```

### 2. Installer les dépendances
Assurez-vous d'avoir Python installé sur votre machine, puis installez les paquets requis :
```bash
pip install Flask Flask-Cors Werkzeug
```

### 3. Lancer le serveur backend
```bash
python server.py
```
> Le serveur se lancera (par défaut configuré en HTTPS adhoc sur l'adresse et le port définis dans le script).

### 4. Lancer le frontend
Ouvrez simplement le fichier `index.html` dans votre navigateur web préféré pour utiliser l'interface graphique.

---

## Auteurs du Projet

Ce projet a été réalisé en collaboration par :

* **Brahim EL BAHLOUL**
  * Étudiant en Master SDA (Sciences de Données et Applications)
  * Faculté Polydisciplinaire de Safi (FPS) et ÉCOLE SUPÉRIEURE DE TECHNOLOGIE-SAFI(EST) 
  
* **ABADA Aziz**
  * Étudiant
  * YouCode UM6P (Université Mohammed VI Polytechnique)

---

> *"Apprendre, construire et sécuriser, ensemble."*