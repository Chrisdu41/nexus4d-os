# Memory Engine v0.4

## Principe
La mémoire NEXUS ne conserve pas tout. Elle conserve ce qui peut modifier une décision future.

## Niveaux
### L0 — Raw Evidence
Données brutes, exports, captures, verbatims, métriques. Peut rester hors dépôt si sensible.

### L1 — Observation
Ce qui a réellement été observé, sans causalité supposée.

### L2 — Learning
Interprétation documentée, avec contexte, confiance et explications alternatives.

### L3 — Pattern
Learning confirmé dans plusieurs expériences ou contextes comparables.

### L4 — Playbook Candidate
Pattern assez robuste pour guider une procédure réutilisable. Nécessite validation humaine avant promotion en playbook.

## Cycle de vie
`proposed → active → challenged → superseded | invalidated | archived`

## Règles de promotion
- Une observation isolée ne devient pas un pattern.
- Un learning doit citer la preuve ou l'expérience qui le supporte.
- Une corrélation ne devient pas causalité par répétition verbale.
- La confiance augmente avec la qualité et la répétition du signal, pas avec l'assurance du modèle.

## Révision
Chaque learning possède :
- `created_at`
- `review_at`
- `confidence`
- `scope`
- `evidence_refs`
- `alternative_explanations`

Un learning périmé doit être réévalué avant d'influencer une décision importante.
