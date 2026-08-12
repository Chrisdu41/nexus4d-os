# Mission Contract v0.2

Toute mission NEXUS 4D OS suit le même contrat afin d'être orchestrable, testable et mémorisable.

## Entrée minimale
- `mission_id`
- `client_id`
- `business_objective`
- `target_audience`
- `offer_or_subject`
- `constraints`
- `available_evidence`
- `deadline`

## États
`intake → context → research → strategy → production → qa → experiment → measurement → learning → done`

Une mission peut sauter une étape seulement si l'information correspondante existe déjà, est datée et reste valide.

## Gates
### G0 — Intake
Objectif métier, audience et définition de terminé compris.

### G1 — Evidence
Faits, sources, inconnues et hypothèses séparés.

### G2 — Strategy
Positionnement, message ou logique d'action suffisamment clairs pour produire sans improviser la stratégie en cours d'exécution.

### G3 — Production
Chaque livrable sert une hypothèse, une audience et une métrique.

### G4 — Quality
Passage des Quality Gates du Core.

### G5 — Experiment
Variable testée, KPI, signal positif/négatif et décision possible définis.

### G6 — Learning
Résultat interprété avec limites et entrée mémoire proposée.

## Sortie obligatoire
- `executive_summary`
- `facts`
- `inferences`
- `hypotheses`
- `decisions`
- `deliverables`
- `kpis`
- `risks`
- `open_questions`
- `next_action`
- `memory_candidate`

## Definition of Done
Une mission n'est pas terminée parce qu'un contenu existe. Elle est terminée quand le décideur sait quoi faire, pourquoi, comment mesurer et ce qu'il faudra apprendre ensuite.
