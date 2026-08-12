# Claude Cowork — Installation et mise à jour

## Principe
GitHub est la source de vérité. Les fichiers `.skill` sont des artefacts installables générés depuis le dépôt.

## Installation manuelle
1. Construire le package avec `scripts/build_cowork_skill.py`.
2. Vérifier le checksum `.sha256`.
3. Dans Claude : Paramètres → Personnaliser → Compétences.
4. Importer le fichier `.skill`.
5. Vérifier que la version affichée correspond à celle du package.

## Mise à jour
Lorsqu'une nouvelle version est publiée :
1. conserver l'ancienne version jusqu'à validation de la nouvelle ;
2. importer le nouveau `.skill` ;
3. exécuter un scénario de test connu ;
4. supprimer l'ancienne version uniquement après validation.

## Important
Installer un nouveau `.skill` ne migre pas automatiquement la mémoire client. Les données clients et learnings appartiennent au système de contexte/mémoire, pas au package de compétence.

## Exemple de build
```bash
python scripts/build_cowork_skill.py \
  --source adapters/claude-cowork/skills/nexus4d-os-orchestrator \
  --output dist \
  --name nexus4d-os-orchestrator
```
