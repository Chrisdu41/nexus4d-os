# NEXUS 4D — Mission Cockpit

## Objectif
Le Mission Cockpit est l'interface opérationnelle de NEXUS 4D OS. Il transforme une mission en poste de pilotage lisible, sans exposer inutilement la complexité interne.

## Vue principale

Le cockpit affiche :
- mission active ;
- client ;
- objectif business ;
- état de la mission ;
- spécialistes mobilisés ;
- données disponibles ;
- données manquantes ;
- livrables ;
- hypothèses ;
- expériences ;
- score qualité ;
- risques ;
- prochaine action ;
- mémoire à mettre à jour.

## États
- `INTAKE`
- `CONTEXT_READY`
- `RESEARCHING`
- `STRATEGY_READY`
- `PRODUCING`
- `QUALITY_REVIEW`
- `READY_TO_TEST`
- `MEASURING`
- `LEARNING`
- `COMPLETE`
- `BLOCKED`

## Carte mission

```yaml
mission_id: M-YYYY-NNN
client_id: string
title: string
objective: string
state: INTAKE
owner: string
specialists: []
quality_score: null
hard_stop: false
next_action: string
```

## Règle UX
Le cockpit doit toujours répondre à trois questions :
1. Où en sommes-nous ?
2. Qu'est-ce qui bloque ?
3. Quelle est la prochaine action utile ?

## Anti-pattern
Ne pas transformer le cockpit en dashboard décoratif rempli de métriques sans décision associée.