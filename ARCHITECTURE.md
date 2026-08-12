# Architecture NEXUS 4D OS

## Couches
**Missions** → Orchestration → Intelligence → Production → Conversion → Learning.

## Flux canonique
`Mission → Context → Orchestrator → Research/VOC → Positioning/Psychology → Creative Hypotheses → Production → Experiment → Measurement → Learning → Client Memory`

## Contrat inter-module
Entrées : `mission_id`, `client_id`, `objective`, `known_facts`, `constraints`, `inputs`, `previous_learnings`.

Sorties : `observations`, `inferences`, `hypotheses`, `deliverables`, `risks`, `open_questions`, `next_recommended_action`.

## Indépendance fournisseur
Les règles métier vivent dans ce dépôt. Les modèles IA sont des moteurs d'exécution interchangeables.

## Source of Truth
1. données client vérifiées ;
2. sources primaires ;
3. données de campagne ;
4. VOC sourcée ;
5. recherche secondaire ;
6. inférence ;
7. hypothèse.

## Anti-patterns
- mega-prompt monolithique ;
- duplication de frameworks ;
- données sans provenance ;
- score présenté comme prédiction ;
- spécialiste hors périmètre.
