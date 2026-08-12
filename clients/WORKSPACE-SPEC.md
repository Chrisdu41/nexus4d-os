# Client Workspace Specification v0.6

## Objectif
Chaque client dispose d'un workspace cohérent qui sépare les faits stables, les actifs, les expériences et les apprentissages.

## Arborescence

```text
clients/<client-id>/
├── profile.md
├── objectives.md
├── audiences.md
├── offers.md
├── positioning.md
├── voice-of-customer.md
├── evidence.md
├── brand.md
├── missions/
├── experiments/
├── learnings/
└── private/
```

## Règles
- `profile.md` contient uniquement des faits relativement stables.
- `missions/` contient les états et livrables de mission.
- `experiments/` contient les tests avec métriques.
- `learnings/` contient uniquement des apprentissages qualifiés.
- `private/` est exclu du versioning public.

## Chargement de contexte
Pour chaque nouvelle mission, charger en priorité :
1. profil ;
2. objectifs ;
3. offres ;
4. audiences ;
5. positionnement ;
6. preuves ;
7. learnings encore valides.

## Fraîcheur
Chaque donnée importante doit pouvoir porter :
- date d'observation ;
- source ;
- niveau de confiance ;
- date de révision.

## Principe
La mémoire client doit réduire le travail répétitif sans figer le raisonnement dans des conclusions anciennes.