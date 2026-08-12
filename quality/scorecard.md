# NEXUS 4D Delivery Scorecard v0.5

Cette scorecard contrôle la qualité d'un livrable. Elle ne prédit ni ventes, ni CPA, ni ROAS.

## Score /100

| Axe | Points | Question |
|---|---:|---|
| Vérité | 10 | Faits, inférences et hypothèses sont-ils séparés ? |
| Clarté | 10 | L'idée centrale est-elle comprise rapidement ? |
| Marketing | 10 | Le livrable sert-il un objectif et une audience précis ? |
| Différenciation | 10 | L'idée évite-t-elle le générique de catégorie ? |
| Preuve | 10 | Les claims importants ont-ils un reason-to-believe ? |
| Vidéo / exécution | 10 | L'exécution rend-elle l'idée plus visible et mémorable ? |
| Neuromarketing | 10 | Attention, compréhension, émotion et décision sont-elles cohérentes ? |
| IA | 10 | L'IA accélère-t-elle sans dégrader vérité et cohérence ? |
| Testabilité | 10 | L'hypothèse peut-elle être invalidée ? |
| Faisabilité | 10 | Les ressources, canal et contraintes sont-ils respectés ? |

## Interprétation

- **90–100** : prêt à exécuter, sous réserve des validations métier.
- **75–89** : solide, corriger les axes faibles avant amplification.
- **60–74** : prototype ; ne pas confondre production et validation.
- **<60** : retravailler la stratégie avant d'investir davantage.

## Hard Stops

Quel que soit le score global, le livrable est bloqué si :

- une preuve essentielle est inventée ;
- le claim principal est indéfendable ;
- l'objectif ou l'audience est inconnu ;
- une donnée sensible est exposée sans nécessité ;
- aucune métrique de validation n'est définie pour une expérience.

## Sortie standard

```yaml
score_total: 0
hard_stop: false
strengths: []
weaknesses: []
required_fixes: []
confidence: low|medium|high
```
