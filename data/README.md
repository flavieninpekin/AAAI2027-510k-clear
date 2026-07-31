# Pre-computed data

Raw measurements used to validate the paper. See `paper/paper.tex` for the
exact definitions (energy gate, kappa, path integral) and the claim hierarchy.

## Reading these files

- `kappa_summary.json` / `all_kappa_raw.csv` / `kappa/` — kappa (gradient
  retention ratio) per algorithm, environment, mode, and seed.
- `path_integral/` — behavioral path length through a 7-dimensional feature
  space across training checkpoints (510K).
- `toy/` — Toy Matching (2-action bandit) results, PPO/A2C/DQN, HIDDEN/REVEALED.
- `transfer/` — policy-transfer and IRL weight recovery (exploratory).

## Caveats (read before use)

1. **kappa is estimator-specific.** Values for PG methods (A2C, PPO,
   REINFORCE) use policy gradients; DQN uses the TD-loss gradient; SAC uses
   the actor gradient. Cross-algorithm comparisons are not meaningful without
   naming the update field (paper, Prop. 4).
2. **Energy gate.** Report kappa only when gradient energy is non-zero. Some
   rows have kappa = 0.5 exactly; under zero (or one-sided) gradient energy
   the ratio falls back to a clamped 0.5 and is NOT a measurement. Some rows
   have kappa = 0.0, which can mean complete cancellation or zero energy.
3. **Uneven campaigns.** Seed counts differ by campaign: e.g. 510K PPO kappa
   has `n=1` for SINGLE/STATIC and `n=9` for DYNAMIC; SAC has `n=2`;
   REINFORCE shows high variance and several zero-energy runs. DQN 510K
   STATIC contains repeated values (3 seeds duplicated), and Overcooked
   contains two unlabeled A2C DYNAMIC sub-campaigns. These rows are retained
   for transparency but should not be pooled as independent seeds.
4. **Reward column** in `all_kappa_raw.csv` is partially empty; reward is not
   reported for all campaigns.

See `experiments/` for the scripts that generated these files.
