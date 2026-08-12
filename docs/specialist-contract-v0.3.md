# Specialist Contract v0.3

Tous les spécialistes NEXUS 4D doivent respecter le même contrat afin que l'orchestrateur puisse les remplacer, les chaîner et auditer leurs sorties.

## Entrée minimale

- `mission_id`
- `client_id`
- `objective`
- `task`
- `facts[]`
- `inferences[]`
- `hypotheses[]`
- `unknowns[]`
- `constraints[]`
- `previous_learnings[]`

## Sortie minimale

- `observations[]`
- `inferences[]`
- `hypotheses[]`
- `deliverables[]`
- `evidence[]`
- `risks[]`
- `open_questions[]`
- `confidence`
- `next_recommended_action`

## Invariants

### I1 — Conservation de la nature des informations
Un fait reste un fait, une hypothèse reste une hypothèse. Le spécialiste peut contester une information mais ne peut pas changer silencieusement son statut.

### I2 — Provenance
Toute donnée externe importante doit conserver une provenance exploitable.

### I3 — Scope
Un spécialiste ne doit pas absorber le rôle d'un autre pour « finir plus vite ». Il retourne une dépendance ou une recommandation de routage.

### I4 — Confidence
`HIGH` ne signifie jamais certitude. Le niveau exprime la confiance dans l'interprétation compte tenu des données disponibles.

### I5 — Memory
Aucun spécialiste sauf `memory` n'écrit une vérité durable dans la mémoire. Les autres produisent des `learning candidates`.

## Failure modes

Le spécialiste doit se déclarer bloqué si :
- une donnée indispensable manque ;
- la mission exige une preuve introuvable ;
- une instruction crée une contradiction avec le Core ;
- une conclusion ne peut pas être distinguée d'une spéculation.

## Definition of Done

Un appel spécialiste est terminé lorsque sa sortie respecte le schéma, le Quality Standard et permet soit l'étape suivante, soit une décision explicite de blocage.
