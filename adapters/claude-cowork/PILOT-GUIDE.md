# Claude Cowork Pilot Guide — NEXUS 4D OS v0.6

## But
Valider NEXUS 4D OS dans un usage réel Cowork sans confondre la logique du dépôt et la couche Skill.

## Préparation
1. Construire le package `.skill` depuis la source du dépôt.
2. Installer le skill orchestrateur dans Claude Cowork.
3. Préparer un client test avec données non sensibles.
4. Choisir une seule mission.

## Mission pilote recommandée
**Créer une campagne Meta Ads** à partir d'une offre existante.

Cette mission couvre suffisamment de couches pour tester :
- contexte ;
- research ;
- VOC ;
- positioning ;
- creative strategy ;
- copywriting ;
- video direction ;
- media buying ;
- quality score ;
- experiment ;
- memory.

## Prompt pilote
```text
Utilise NEXUS 4D OS pour créer une campagne Meta Ads pour ce client.
Avant de produire les publicités, construis la mission, charge le contexte disponible, distingue faits/inférences/hypothèses, puis suis le workflow NEXUS jusqu'au plan de test et à la proposition de mémoire.
```

## Ce qu'il faut observer
- le bon workflow est-il choisi ?
- Claude demande-t-il uniquement les informations réellement bloquantes ?
- les rôles restent-ils distincts ?
- les claims sont-ils défendables ?
- la scorecard bloque-t-elle les sorties faibles ?
- la prochaine action est-elle claire ?
- le learning proposé est-il réutilisable ?

## Rapport pilote
Classer chaque problème :
- `BLOCKER`
- `MAJOR`
- `MINOR`
- `UX`
- `DOCUMENTATION`

Ne corriger le Core qu'après avoir déterminé si le problème vient du Core, de la Mission, du Specialist ou de l'adapter Cowork.