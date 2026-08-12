# Cowork Pilot Runbook — CT PROD / NEXUS 4D Meta Ads

## 1. Installer le skill pilote
Importer `nexus4d-os-orchestrator.skill` dans Claude → Paramètres → Personnaliser → Compétences.

## 2. Ouvrir une nouvelle conversation Cowork
Ne pas mélanger ce pilote avec une ancienne conversation contenant des hypothèses non contrôlées.

## 3. Prompt de départ

```text
Utilise NEXUS 4D OS pour piloter cette mission Meta Ads.

Contexte : CT PROD souhaite tester une campagne de génération de leads autour de la méthode NEXUS 4D, qui combine Vidéo, Marketing, IA et Neuromarketing.

Objectif du pilote : concevoir une première vague de tests Meta Ads ET tester la qualité du système NEXUS 4D OS lui-même.

Avant toute création :
1. sépare FACTS / INFERENCES / HYPOTHESES / UNKNOWNS ;
2. indique les inconnues réellement bloquantes ;
3. ne fabrique aucun prix, témoignage, performance ou verbatim ;
4. si une information non bloquante manque, avance avec une hypothèse explicitement marquée ;
5. exécute les rôles nécessaires dans l'ordre ;
6. termine avec une NEXUS Delivery Scorecard, la prochaine action et un Learning Candidate sur le fonctionnement du système.
```

## 4. Ce que l'on observe
Noter sans corriger pendant le premier run :
- demande-t-il trop de précisions ?
- commence-t-il à créer trop tôt ?
- conserve-t-il la séparation faits/hypothèses ?
- les angles sont-ils réellement distincts ?
- les spécialistes ont-ils des sorties différentes ?
- les KPI correspondent-ils à l'objectif ?
- la scorecard révèle-t-elle de vraies faiblesses ?
- la prochaine action est-elle concrète ?

## 5. Stop conditions
Arrêter le run si Cowork :
- invente une preuve ;
- invente un résultat ;
- utilise un faux verbatim ;
- présente un score comme prédiction de ROAS ;
- ignore une inconnue critique et construit quand même une recommandation définitive.

## 6. Après le run
Remplir `pilot-observation-log.md`, puis décider :
- KEEP : comportement correct ;
- FIX : comportement à corriger ;
- REMOVE : complexité inutile ;
- ADD : capacité réellement manquante.
