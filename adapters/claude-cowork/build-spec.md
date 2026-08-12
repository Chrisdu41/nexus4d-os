# Cowork Skill Build Spec v0.4

## Objectif
Construire des fichiers `.skill` reproductibles à partir des sources versionnées du dépôt.

## Principe
Le fichier `.skill` est un artefact de distribution. Il ne doit jamais devenir la source de vérité.

## Pipeline
1. Valider `package-manifest.yaml`.
2. Lire l'entrypoint `SKILL.md`.
3. Résoudre les références nécessaires.
4. Copier uniquement les fichiers autorisés dans un dossier temporaire unique.
5. Vérifier qu'aucun secret ou chemin absolu local n'est présent.
6. Compresser le dossier en ZIP.
7. Renommer l'archive en `.skill`.
8. Calculer un checksum SHA-256.
9. Publier l'artefact dans `dist/` ou une Release GitHub.

## Structure attendue
```text
nexus4d-os-orchestrator/
├── SKILL.md
└── references/
```

## Versioning
La version du package suit SemVer. Une modification de logique incompatible augmente la version majeure ; une nouvelle capacité compatible augmente la mineure ; une correction augmente le patch.

## Interdiction
Ne pas embarquer automatiquement les dossiers `clients/`, `outputs/`, données brutes, credentials ou exports CRM/Ads.
