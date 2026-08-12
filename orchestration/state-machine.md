# Mission State Machine

## États

### INTAKE
La demande est reçue mais pas encore normalisée.

### CONTEXT
Le système collecte les faits, inconnues, contraintes et apprentissages existants.

### PLAN
L'orchestrateur choisit la mission, les spécialistes, l'ordre et les gates.

### EXECUTE
Les spécialistes exécutent leurs tâches selon leurs contrats.

### QA
Le système applique les Quality Gates NEXUS 4D.

### DELIVER
Les livrables, décisions, KPI et risques sont consolidés.

### LEARN
Le système produit un `learning candidate` à partir de la mission.

### DONE
Mission terminée.

## Blocages

### BLOCKED_INPUT
Une entrée utilisateur indispensable manque et n'est pas raisonnablement inférable ou recherchable.

### BLOCKED_EVIDENCE
La décision exige une preuve indisponible.

### FAILED_QA
Le livrable échoue à un ou plusieurs gates critiques.

### CANCELLED
Mission arrêtée volontairement.

## Transitions autorisées

```text
INTAKE → CONTEXT
CONTEXT → PLAN | BLOCKED_INPUT
PLAN → EXECUTE | BLOCKED_EVIDENCE
EXECUTE → QA | BLOCKED_INPUT | BLOCKED_EVIDENCE
QA → DELIVER | EXECUTE | FAILED_QA
DELIVER → LEARN
LEARN → DONE
```

## Règle
Un état bloqué doit toujours exposer : cause, donnée requise, impact et action de déblocage.
