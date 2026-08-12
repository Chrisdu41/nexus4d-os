# Sprint 3 — Acceptance Tests

## A1 — Mission schema
Un état de mission valide doit pouvoir représenter faits, inférences, hypothèses, inconnues, étapes, KPI et learning candidate.

## A2 — Specialist schema
Tout spécialiste doit accepter le contrat d'entrée commun et retourner le contrat de sortie commun.

## A3 — No silent promotion
Une hypothèse ne peut pas devenir un fait sans preuve ajoutée.

## A4 — Routing
Les 12 missions disposent d'une séquence de spécialistes dans `routing-matrix.yaml`.

## A5 — Scope isolation
Un spécialiste doit signaler une dépendance plutôt que reproduire silencieusement le travail d'un autre spécialiste.

## A6 — Memory write control
Seul le rôle `memory` possède `can_write_memory: true`.

## A7 — Evidence requirement
Research et VOC conservent la provenance des données lorsque des sources existent.

## A8 — Performance data
Le spécialiste Performance ne peut conclure sur des performances réelles sans métriques observées.

## A9 — Cowork honesty
L'adapter Cowork ne prétend pas lancer des agents natifs en parallèle lorsque la capacité n'est pas disponible.

## A10 — Quality gate
Une mission échouant à un gate critique ne peut passer directement à `DELIVER`.

## Definition of Done Sprint 3
- schemas machine-readable présents ;
- registre spécialistes présent ;
- routing matrix présente ;
- state machine documentée ;
- adapter Cowork documenté ;
- source du skill orchestrateur Cowork présente ;
- tests d'acceptation définis.
