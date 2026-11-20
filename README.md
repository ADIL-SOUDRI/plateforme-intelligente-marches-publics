# Plateforme intelligente d'assistance aux marchés publics basée sur le RAG et le Machine Learning

![Python](https://img.shields.io/badge/Python-FastAPI-009688)
![Next.js](https://img.shields.io/badge/Next.js-React-000000)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-ChromaDB-336791)
![Docker](https://img.shields.io/badge/Docker-Compose-2496ED)

## Sommaire

- [Présentation](#présentation)
- [Objectifs](#objectifs)
- [Fonctionnalités](#fonctionnalités)
- [Pipeline RAG](#pipeline-rag)
- [Classification automatique](#classification-automatique-des-documents)
- [Architecture technique](#architecture-technique)
- [Installation](#installation-et-configuration)
- [Structure du projet](#structure-du-projet)
- [Sécurité](#sécurité)
- [Perspectives d'amélioration](#perspectives-damélioration)
- [Auteur](#auteur)

## Présentation

Cette plateforme web facilite l'accès aux informations relatives aux marchés publics. Un chatbot permet de poser des questions en langage naturel et d'obtenir des réponses contextualisées à partir des documents réglementaires de référence et des fichiers PDF importés par l'utilisateur.

Elle repose sur une architecture **RAG** qui combine une recherche documentaire hybride et un modèle de langage (LLM), ainsi que sur un module de **Machine Learning** qui classe automatiquement les documents par domaine.

## Objectifs

- Simplifier la consultation des documents relatifs aux marchés publics.
- Permettre l'interrogation des documents en langage naturel.
- Fournir des réponses pertinentes et fondées sur les sources documentaires.
- Faciliter l'importation et la gestion des documents PDF.
- Automatiser la classification des documents par domaine.
- Assurer une gestion sécurisée des utilisateurs et de leurs conversations.

## Fonctionnalités

### Espace utilisateur

- Inscription et authentification sécurisée.
- Gestion du profil.
- Importation et gestion des documents PDF personnels.
- Interaction avec un chatbot intelligent.
- Consultation de l'historique des conversations.
- Réponses contextualisées avec références aux documents.

### Espace administrateur

- Gestion des comptes utilisateurs.
- Ajout, consultation et gestion des documents de référence.
- Gestion des documents exploités par le chatbot.
- Suivi de l'historique des conversations.
- Administration de la plateforme.

## Pipeline RAG

Le système recherche les passages pertinents dans les documents avant de générer une réponse avec le LLM.

1. Extraction du contenu des documents PDF.
2. Nettoyage et structuration du texte.
3. Découpage des documents en segments (*chunking*).
4. Génération des *embeddings* avec BGE-M3.
5. Stockage des embeddings dans ChromaDB.
6. Recherche hybride : recherche vectorielle + BM25.
7. Transmission des passages pertinents au LLM via LangChain.
8. Génération d'une réponse contextualisée avec Google Gemini.

## Classification automatique des documents

Un module de Machine Learning prédit le domaine d'un document.

- **TF-IDF** : transformation du texte en caractéristiques numériques.
- **Logistic Regression** : classification des documents.
- **Scikit-learn** : entraînement et utilisation du modèle.

Domaines possibles : bâtiment, génie civil, électricité, informatique, maintenance.

## Architecture technique

| Couche | Technologies |
|---|---|
| Frontend | Next.js, React, TypeScript, Tailwind CSS |
| Backend | Python, FastAPI |
| ORM | SQLAlchemy |
| Validation des données | Pydantic |
| Base de données relationnelle | PostgreSQL |
| Base de données vectorielle | ChromaDB |
| Embeddings | BGE-M3 |
| Recherche documentaire | BM25, recherche vectorielle hybride |
| Orchestration RAG | LangChain |
| Modèle de langage | Google Gemini |
| Machine Learning | Scikit-learn, TF-IDF, Logistic Regression |
| Authentification | JWT |
| Conteneurisation | Docker, Docker Compose |
| Documentation et tests API | Swagger UI |
| Gestion de versions | Git, GitHub |

### Schéma général

```text
                   UTILISATEUR
                        |
                        v
               FRONTEND - NEXT.JS
                 React / Tailwind
                        |
                        v
                BACKEND - FASTAPI
                        |
             +----------+----------+
             |                     |
             v                     v
       POSTGRESQL              MODULE IA
       SQLAlchemy                  |
                             +-----+------+
                             |            |
                             v            v
                         PIPELINE RAG   MACHINE LEARNING
                             |            |
                         BGE-M3       TF-IDF
                             |            |
                         ChromaDB   Logistic Regression
                             |
                         Recherche hybride
                      (Vectorielle + BM25)
                             |
                         LangChain
                             |
                       GOOGLE GEMINI
                             |
                             v
                    RÉPONSE CONTEXTUALISÉE
```

## Installation et configuration

### Prérequis

- Python
- Node.js et npm
- Docker et Docker Compose
- Git
- Une clé API Google Gemini

### 1. Cloner le projet

```bash
git clone <URL_DU_DEPOT>
cd <NOM_DU_PROJET>
```

### 2. Configurer le backend

```bash
cd backend
python -m venv .venv
```

Activer l'environnement virtuel (Windows) :

```bash
.venv\Scripts\activate
```

Installer les dépendances :

```bash
pip install -r requirements.txt
```

Créer un fichier `.env` dans `backend/` :

```env
DATABASE_URL=postgresql://USER:PASSWORD@localhost:5434/marches_publics
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
JWT_SECRET_KEY=YOUR_SECRET_KEY
```

> Ne publie jamais le fichier `.env` sur GitHub. Ajoute-le au `.gitignore` et fournis un `.env.example`.

### 3. Lancer les services Docker

À la racine du projet :

```bash
docker compose up -d
```

Cette commande démarre PostgreSQL et ChromaDB.

### 4. Démarrer le backend

```bash
uvicorn app.main:app --reload
```

Documentation interactive des API (Swagger UI) : <http://localhost:8000/docs>

### 5. Configurer et démarrer le frontend

Dans un autre terminal :

```bash
cd frontend
npm install
```

Créer le fichier `.env.local` :

```env
NEXT_PUBLIC_API_URL=http://localhost:8000
```

Démarrer l'application :

```bash
npm run dev
```

Application disponible sur : <http://localhost:3000>

## Structure du projet

```text
project/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── services/
│   │   ├── database/
│   │   ├── rag/
│   │   ├── ml/
│   │   └── main.py
│   ├── requirements.txt
│   └── .env.example
├── frontend/
│   ├── app/
│   ├── components/
│   ├── services/
│   ├── public/
│   ├── package.json
│   └── .env.example
├── data/
│   └── documents.csv
├── docker-compose.yml
└── README.md
```

## Sécurité

- Authentification basée sur JWT.
- Gestion des rôles et des autorisations.
- Protection des routes selon les droits des utilisateurs.
- Clés API et informations sensibles stockées dans des variables d'environnement.

## Perspectives d'amélioration

- Découpage plus intelligent des documents juridiques.
- Optimisation de la pertinence de la recherche hybride.
- Ajout d'un mécanisme de *reranking* des passages récupérés.
- Enrichissement du dataset pour améliorer le classificateur.
- Meilleure évaluation de la qualité des réponses générées.
- Prise en charge de formats documentaires supplémentaires.

## Auteur

**Adil SOUDRI** : Étudiant ingénieur en Génie Informatique, FST Settat

Projet réalisé lors d'un stage PFA chez **BC Skills Group, Safi** (juillet – août 2026).

Contact : [adilsoudri@gmail.com](mailto:adilsoudri@gmail.com)

---

*Projet de développement Full Stack, Intelligence Artificielle, RAG et Machine Learning.*