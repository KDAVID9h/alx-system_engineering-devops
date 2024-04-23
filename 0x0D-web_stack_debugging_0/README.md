# Projet de Débogage Docker - Page "Hello Holberton"

Ce projet vise à résoudre un problème de configuration dans un conteneur Docker afin de faire fonctionner Apache et de retourner une page contenant "Hello Holberton" lorsqu'on interroge la racine du serveur.

## Objectif

Le but de ce projet est de :

- Lire attentivement la page conceptuelle Docker pour comprendre les bases de Docker et son fonctionnement.
- Démarrer un conteneur Docker en utilisant l'image `holbertonschool/265-0`.
- Vérifier l'état du conteneur et utiliser curl pour interroger le port 8080 afin de vérifier si la page est correctement servie.
- Accéder au conteneur et identifier et corriger les problèmes de configuration d'Apache.
- Tester à nouveau en utilisant curl pour vérifier si le port 80 retourne désormais une page contenant "Hello Holberton".

## Instructions

1. Lire attentivement la page conceptuelle Docker.
2. Démarrer un conteneur Docker en utilisant la commande `docker run -p 8080:80 -d -it holbertonschool/265-0`.
3. Vérifier l'état du conteneur en utilisant `docker ps`.
4. Utiliser curl pour interroger le port 8080 avec la commande `curl 0:8080`.
5. Accéder au conteneur en utilisant la commande `docker exec -it <ID_DU_CONTENEUR> /bin/bash`.
6. Identifier et corriger les problèmes de configuration d'Apache.
7. Tester à nouveau en utilisant curl pour vérifier si le port 80 retourne désormais une page contenant "Hello Holberton".
8. Copier les commandes utilisées pour corriger le problème dans le fichier de réponse.

---

Ce projet fait partie du cursus de formation en ingénierie des systèmes et DevOps à Holberton School.
