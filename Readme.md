# Network Analyzer 🔎

## Description

**Network Analyzer** est un projet Python permettant d'analyser un ensemble de données représentant des appareils présents sur un réseau.

Le programme identifie notamment les appareils actifs, les adresses IP uniques, les ports utilisés, les appareils utilisant SSH ainsi que certains ports considérés comme sensibles.

Ce projet constitue une première étape dans mon apprentissage de Python appliqué aux réseaux et à la cybersécurité.

## Fonctionnalités

- 📊 **Comptage du nombre total d'appareils**
- 🟢 **Identification du nombre d'appareils actifs**
- 🌐 **Extraction des adresses IP uniques**
- 🔌 **Identification des ports utilisés**
- 🔐 **Détection des appareils utilisant SSH** (port 22)
- ⚠️ **Détection de certains ports sensibles** :
  - `21` — FTP
  - `22` — SSH
  - `23` — Telnet
  - `3389` — RDP
- 📋 **Génération d'un rapport réseau lisible**

## Technologies

- Python 3
- Listes et dictionnaires
- Boucles `for`
- Conditions `if`
- Fonctions et `return`
- Manipulation de données structurées

## Exemple de sortie

Pour un réseau contenant plusieurs appareils, le programme génère un rapport similaire à :

```text
===== RAPPORT RÉSEAU =====
Nombre total d'appareils : 5
Appareils actifs : 3
IPs uniques : 4
Ports utilisés : 4
Appareils actifs avec SSH : 1

===== PORTS SENSIBLES =====
192.168.1.10 → Port 22
192.168.1.25 → Port 21
===========================
```

## Compétences développées

Ce projet m'a permis de pratiquer :

- La manipulation de listes et de dictionnaires ;
- La création et l'utilisation de fonctions Python ;
- Les boucles et conditions ;
- La déduplication de données ;
- L'association de clés et de valeurs avec les dictionnaires ;
- L'analyse de données représentant un environnement réseau ;
- La génération automatique d'un rapport.

## Installation et utilisation

1. **Cloner le dépôt :**
   ```bash
   git clone <URL_DU_DEPOT>
   ```

2. **Accéder au dossier :**
   ```bash
   cd network-analyzer
   ```

3. **Lancer le programme :**
   ```bash
   python network_analyzer.py
   ```

> *Aucune bibliothèque externe n'est nécessaire.*

## Structure du projet

```text
network-analyzer/
│
├── network_analyzer.py
└── README.md
```

## Évolutions prévues

Ce projet constitue une première version. Des améliorations pourront être ajoutées progressivement :

- Analyse de données réseau réelles ;
- Utilisation de sockets Python ;
- Récupération d'informations réseau automatiquement ;
- Détection d'anomalies ;
- Amélioration du système de rapport ;
- Intégration avec des outils Linux ;
- Ajout de tests automatisés.

## Objectif du projet

L'objectif principal est de construire progressivement des compétences en Python, réseaux et cybersécurité, avant de développer des projets plus avancés utilisant de véritables données réseau et des techniques d'analyse de sécurité.
