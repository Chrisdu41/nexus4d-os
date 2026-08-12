# Adapter — Claude Cowork

Cet adapter traduit NEXUS 4D OS en Skills compatibles avec Claude Cowork sans déplacer la logique métier hors du dépôt.

## Principe

Les fichiers `.skill` sont des packages de distribution. Ils ne sont **pas** la source de vérité.

Source de vérité :
- `core/`
- `missions/`
- `specialists/`
- `orchestration/`

Distribution Cowork :
- `adapters/claude-cowork/skills/`

## Orchestrator Skill

Le skill orchestrateur doit :
1. identifier la mission ;
2. appliquer `routing-matrix.yaml` ;
3. imposer le contrat spécialiste ;
4. conserver la séparation FACT / INFERENCE / HYPOTHESIS / UNKNOWN ;
5. contrôler les gates ;
6. produire un learning candidate ;
7. ne jamais prétendre que plusieurs skills Cowork ont réellement exécuté en parallèle si l'environnement ne le permet pas.

## Limite importante

Claude Cowork peut sélectionner des Skills selon leur description, mais l'orchestration multi-agent réelle dépend des capacités du produit. L'adapter doit donc fonctionner en deux modes :

### Mode A — Skill orchestration
L'orchestrateur applique successivement les rôles spécialistes dans le même contexte.

### Mode B — Native multi-agent
À utiliser uniquement si l'environnement fournit explicitement une primitive d'agents ou de délégation.

Le système ne doit jamais simuler une capacité native absente.
