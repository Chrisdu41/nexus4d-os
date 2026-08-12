# Experiment Protocol v0.4

## Objectif
Faire de chaque test une source d'apprentissage, pas seulement un résultat de campagne.

## Contrat d'expérience
Chaque expérience doit déclarer :
- `experiment_id`
- `mission_id`
- `client_id`
- hypothèse falsifiable
- variable principale
- contrôle ou référence
- audience
- exécution
- KPI principal
- fenêtre de mesure
- critères de lecture
- résultat
- interprétation
- explications alternatives
- décision suivante

## Règle de causalité
Si plusieurs variables majeures changent simultanément, le résultat peut être utile opérationnellement mais ne doit pas être présenté comme preuve causale d'une variable isolée.

## Décisions autorisées
- `iterate`
- `scale`
- `hold`
- `stop`
- `retest`
- `insufficient_evidence`

## Sortie mémoire
Une expérience terminée peut proposer zéro, un ou plusieurs learnings. Le module Memory valide leur forme et leur niveau de confiance avant archivage.
