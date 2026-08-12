# NEXUS 4D OS — Intake Gate v0.7

## Objectif
Empêcher le routage prématuré des spécialistes lorsqu'une mission manque d'intrants critiques.

## Étape 0 obligatoire
Avant toute recherche, stratégie ou production, classer chaque champ :
- `available` — information fournie ou vérifiée ;
- `assumable` — information manquante mais une hypothèse explicite permet de concevoir sans créer un risque majeur ;
- `blocking` — information indispensable à la prochaine étape ;
- `not_applicable` — non pertinente pour cette mission.

## Champs universels
1. `business_objective`
2. `audience_or_icp`
3. `offer_definition`
4. `conversion_destination`
5. `evidence_available`
6. `constraints`
7. `measurement_capability`

## Champs conditionnels
- `price` — bloquant uniquement si nécessaire à l'économie, la promesse ou au CTA ;
- `budget` — bloquant pour un plan média chiffré, pas pour créer une architecture de test ;
- `tracking_access` — bloquant pour lancement/mesure, pas pour concept ;
- `voice_of_customer` — recommandé avant copy final ; peut être `deferred` pour prototypage ;
- `brand_context` — peut être assumable si le ton par défaut est explicitement déclaré.

## Décision
### GO — Design
La mission peut avancer en conception si les champs manquants sont `assumable` et explicitement marqués.

### GO — Launch
Le lancement n'est autorisé que si tous les hard blockers de la mission sont `available`.

### STOP
Arrêter et demander une information lorsqu'une étape suivante dépend d'un champ `blocking`.

## Routage spécialiste
Chaque rôle reçoit un statut :
- `ready`
- `deferred`
- `blocked`
- `completed`

Un rôle `blocked` ne doit pas être présenté comme exécuté. Un rôle `deferred` peut produire un plan de collecte, mais ce plan n'est pas compté comme analyse réalisée.

## Claim Ledger
Avant Creative final, Copy final ou livraison :

| Claim | Type | Source | Statut |
|---|---|---|---|
| texte du claim | fact / inference / hypothesis | URL, fichier, donnée client ou null | verified / unsupported / remove |

Tout claim chiffré sans source = `unsupported` → supprimer ou sourcer.

## Scorecard
La seule scorecard de livraison autorisée est `quality/scorecard.md` (/100). Les variantes ad hoc sont interdites.
