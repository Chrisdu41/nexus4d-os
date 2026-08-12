# Orchestration Layer v0.3

Cette couche transforme les Missions NEXUS 4D en séquences exécutables par un moteur IA.

## Responsabilités

- charger la mission et le contexte client ;
- identifier les spécialistes nécessaires ;
- ordonner les dépendances ;
- imposer les quality gates ;
- propager faits, inconnues et hypothèses ;
- consolider les livrables ;
- préparer l'entrée mémoire ;
- arrêter proprement une mission si une donnée indispensable manque.

## Principe

L'orchestrateur ne remplace pas les spécialistes. Il contrôle leur séquence et la cohérence du système.

## State machine

`INTAKE → CONTEXT → PLAN → EXECUTE → QA → DELIVER → LEARN → DONE`

États d'exception :

- `BLOCKED_INPUT`
- `BLOCKED_EVIDENCE`
- `FAILED_QA`
- `CANCELLED`

## Règle de vérité

Aucune étape suivante ne peut transformer une `HYPOTHESIS` en `FACT` sans nouvelle preuve.
