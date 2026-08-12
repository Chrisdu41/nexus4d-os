# Sprint 7 — Audit du premier run réel Cowork

## Verdict
Le pilote valide la direction générale, mais révèle 4 défauts structurels à corriger avant de considérer NEXUS 4D OS comme prêt pour une utilisation répétable.

## KEEP
- séparation FACTS / INFERENCES / HYPOTHESES / UNKNOWNS ;
- anti-fabrication réellement appliqué ;
- blocage de la preuve lorsque la preuve manque ;
- test par angle avant test de hook/format ;
- décisions média en relatif plutôt qu'avec des seuils universels ;
- Learning Candidate produit en fin de mission ;
- distinction entre conception et lancement.

## FIX
### F1 — Intake Gate absent
Le système route les spécialistes avant d'avoir vérifié les intrants critiques. Research, VoC et une partie du Copywriter ont donc tourné sans matière exploitable.

Correction : rendre l'Intake Gate obligatoire avant le routage.

### F2 — Scorecard non canonique
Le dépôt définit une Delivery Scorecard /100, mais le pilote a créé une scorecard ad hoc /35. Cela crée une divergence de gouvernance.

Correction : interdire toute scorecard alternative. La sortie doit utiliser `quality/scorecard.md` et ses Hard Stops.

### F3 — Claims non sourcés malgré l'anti-fabrication
La phrase « c'est là que 90 % des créateurs bloquent » a été générée sans preuve. Le système n'a donc pas totalement tenu son propre garde-fou.

Correction : tout nombre, proportion ou comparaison factuelle doit être soit sourcé, soit supprimé, soit marqué HYPOTHESIS si réellement testable.

### F4 — Confusion entre bloquant pour lancer et bloquant pour concevoir
L'offre et la destination sont effectivement bloquantes pour finaliser une campagne. En revanche, le prix n'est pas toujours nécessaire pour une campagne lead-gen top-of-funnel. Le système a sur-bloqué U1 en regroupant offre + prix.

Correction : séparer `offer_definition` et `price`. Le prix n'est hard-blocker que s'il influence la promesse, l'économie du test ou le CTA.

## REMOVE
- scorecards improvisées ;
- pourcentages ou statistiques génériques non sourcés ;
- formulation « les rôles ont tourné » lorsqu'un rôle n'a fait qu'émettre un plan de collecte ; utiliser `deferred` ou `blocked` ;
- hypothèses ICP trop larges servant immédiatement de base au copy sans validation minimale.

## ADD
- Intake Gate v0.7 ;
- statut par spécialiste : `ready | deferred | blocked | completed` ;
- Claim Ledger : chaque claim important = source / statut / propriétaire ;
- Evidence Gate avant Copy et Creative final ;
- scorecard canonique /100 obligatoire ;
- Run Review avec KEEP / FIX / REMOVE / ADD après chaque pilote.

## Learning validé
**L-007-001** — Une mission complexe ne doit pas router les spécialistes tant que les intrants critiques n'ont pas été classés en `available`, `assumable` ou `blocking`.

Niveau : L1 (pilot observation). Ne pas promouvoir en pattern global avant réplication sur d'autres missions.

## Prochain test
Relancer exactement la même mission avec Intake Gate v0.7 et comparer :
- nombre de rôles réellement exécutés ;
- nombre d'hypothèses non nécessaires ;
- nombre de claims non sourcés ;
- temps jusqu'au premier livrable exploitable ;
- score Delivery /100 ;
- nombre de Hard Stops.
