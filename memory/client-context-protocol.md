# Client Context Protocol v0.4

## Objectif
Définir le paquet minimal de contexte qu'une mission doit charger avant toute décision importante.

## Sections
1. `identity` — client_id, nom, secteur, territoire, langue.
2. `business` — modèle économique, offre, pricing, marge si disponible.
3. `audiences` — ICP, segments, exclusions.
4. `positioning` — promesse, catégorie, mécanisme, différenciation.
5. `evidence` — preuves, cas clients, témoignages, sources.
6. `constraints` — budget, délai, équipe, conformité, canaux.
7. `active_goals` — objectifs business et KPI.
8. `known_learnings` — apprentissages qualifiés encore valides.
9. `open_questions` — inconnues qui peuvent modifier une décision.

## Règles
- Chaque élément important doit avoir `source`, `updated_at` et `confidence` lorsque pertinent.
- Une donnée absente reste absente : ne jamais la compléter silencieusement.
- Les données temporelles doivent porter une date de révision.
- Les informations sensibles peuvent être référencées sans être committées dans GitHub.

## Ordre de confiance
Donnée client vérifiée > donnée de campagne > source primaire > VOC sourcée > source secondaire > inférence > hypothèse.
