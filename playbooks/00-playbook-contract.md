# Playbook Contract v0.5

Un playbook est une séquence reproductible destinée à exécuter une mission ou une sous-mission.

## Contrat minimal

Chaque playbook doit définir :

- `purpose` — résultat recherché ;
- `trigger` — quand l'utiliser ;
- `inputs` — données minimales ;
- `specialists` — rôles mobilisés ;
- `steps` — séquence ;
- `gates` — conditions de passage ;
- `outputs` — livrables ;
- `metrics` — signaux à observer ;
- `memory_write` — ce qui peut être proposé à la mémoire ;
- `failure_modes` — erreurs fréquentes ;
- `definition_of_done` — critère de fin.

## Règle d'or

Un playbook n'est pas un script rigide. Il formalise ce qui doit rester stable tout en laissant les décisions contextuelles ouvertes.

## Gate universel

Avant toute production :

1. audience connue ;
2. objectif connu ;
3. hypothèse explicite ;
4. preuve disponible ou manque identifié ;
5. métrique définie.

Si l'un de ces éléments manque et qu'il conditionne le résultat, le playbook doit se mettre en état `BLOCKED` ou lancer une étape de recherche.
