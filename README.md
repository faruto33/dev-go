
# PARIS 2024 FAQ

Bienvenu sur le projet FAQ paris 2024 livré pour la société dev&Go.

Il a été divisé en 2 projets distincts:

- La création d'une **API BACKEND** pour livrer les questions/réponses et les catégories à partir du dataset extrait sur kaggle :
https://www.kaggle.com/datasets/sahityasetu/paris-2024-olympics-faq

- La création d'une interface **FRONTEND** pour intéragir avec un utilisateur qui souhaite rechercher une question/réponse.

### le BACKEND ###

Le projet a suivi les étapes de développement suivantes:
- Analyse du dataset kaggle sous **jupyter notebook** pour comprendre la structure et être en mesure de l'exploiter
- Installation de l'environnement de travail local **fastAPI** et **Python**
- Recherche d'un moteur de recherche sémantique **performant** et surtout **gratuit** qui permet de livrer les questions/réponses en fonction de mots/clés. Après plusieurs essais infructueux : **elasticsearch**, entrainement d'un **transformer hugging face** avec **FAISS index**, **txtai**, j'ai finalement opté pour un modèle d'embeddings avec le modèle **bert** et la librairie **sentence-transformer (https://sbert.net/)** qui offre des performances et pertinence de résultat correctes.
- Developpement du système de recherche par **catégorie** après extraction dans le dataset
- Déploiement dans le **cloud google GCP** après **conteneurisation sous docker**, après un test infructueux sur **heroku** (la solution est devenue payante)
- Testable ici : https://dev-go-faq-902037774966.europe-west1.run.app/docs 


### le FRONTEND ###

Le projet a suivi les étapes de développement suivantes:
- Installation d'un environnement local utilisant **vue.js 3** et le **bundler vite**
- Création du squelette html de la page avec **bootstrap** et des **composants vue** : header, home , search, tree , breadcrumb, loader
- Codage des différents composants, des dépendances, des interactions, des appels API, installation de librairies npm : **vue3-treeview, awesome font, vue-content-loader, axios**
- Une fois l'appli testée et le rendu satisfaisant en local, déploiement dans le **cloud google GCP** après **conteneurisation sous docker**









## GESTION DE PROJET

- La gestion de projet a été réalisé sour **Trello** : https://trello.com/b/HBLypEpR/devgo-faq avec 2 cartes principales, **backend** et **frontend** et associé a un **diagramme de Gantt** sur le plugin teamGantt : https://app.teamgantt.com/projects/gantt?ids=4072120. Chaque carte a été mise à jour au fil du temps avec des commentaires sur les difficultés rencontrées et la mise à jour du taux d'achèvement.
- Un entrepôt **github** a également été utilisé pour stocker l'intégralité du code de l'application : https://github.com/faruto33/dev-go, avec des commits réguliers.


## REMARQUES

- J'ai choisi de travailler directement sur la branche github principale dans un soucis de simplicité et de gain de temps
- Je n'ai pas codé de test unitaire, également dans un soucis de gain de temps, et surtout j'étais tout seul à évoluer sur le projet.
- J'ai  privilégié le rendu "desktop" de l'application, plutot que le rendu "mobile" qui n'est pas exceptionnel

## AMELIORATIONS

De nombreuses pistes d'améliorations sont possibles :
- Améliorer le rendu sur mobile
- Tester d'autres outils de recherche sémantique (elastic)
- Ajouter un router et des urls sur l'appli (dans une optique SEO)
- Faire un système de filtre, un breadcrumb 
- Faire la version FAQ anglaise (présente aussi dans le dataset mais volontairement mise de côté)
- Ajouter un système de pagination des résultats, ou un infinite scroll

et bien d'autres choses encore...

## TESTS

L'application est testable à l'url suivante : https://dev-go-faq-frontend-902037774966.europe-west1.run.app/

Cela peut prendre plusieurs secondes avant de la voir s'afficher en raison d'un temps de chargement pour accéder à l'API. Une fois la page d'accueil complètement affichée, l'interface devient fluide et rapide.




## API Reference

#### Rechercher les réponses

```http
  GET /search?keyword=keyword&category=$category&limit=$limit
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `keywords` | `string` | Rechercher la réponse par mots-clés  |
| `category` | `string` | Rechercher la réponse par catégorie  |
| `limit`    | `int` | Nombre de réponses à renvoyer |

#### Recupérer la liste de toute les catégories

```http
  GET /category
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `/`      | `void` | Récupère la liste de toute les catégories |

#### La document complète est disponibles ici

https://dev-go-faq-902037774966.europe-west1.run.app/redoc


## Authors

- [@farid machrou](https://github.com/faruto33/)

