# IIGC — Information-Induced Gradient Contraction in MARL

Code for AAAI 2027 paper. Investigates how hidden relational information causes policy gradient cancellation in multi-agent RL.

## Quick Start

```bash
# Install
pip install -e .

# Import environment
from iigc.env import FiveTenKEnv
env = FiveTenKEnv(mode='dynamic', num_players=4)

# Train PPO with self-play
from iigc.train import train_ppo_selfplay
model = train_ppo_selfplay(mode='single', total_timesteps=1_000_000, seed=42)
```

## Reproduce Paper Results

```bash
# Full reproduction (requires GPU, ~25h)
python experiments/reproduce_all.py

# Quick check (uses pre-computed data)
python experiments/reproduce_all.py --quick

# Specific experiments
python experiments/reproduce_kappa.py --env 510k --algo ppo
python experiments/reproduce_path.py

# Generate figures
python experiments/reproduce_figures.py
```

## Structure

| Path | Description |
|------|-------------|
| `src/iigc/` | Main package (`import iigc`) |
| `src/iigc/env/` | Environments: 510K, Toy, wrappers |
| `src/iigc/train/` | Training algorithms (PPO, DQN, A2C, SAC, REINFORCE) |
| `src/iigc/eval/` | Analysis (kappa, path integral, IRL, stability, transfer) |
| `overcooked_adapt/` | Overcooked environment adaptation |
| `experiments/` | Reproduction scripts |
| `data/` | Pre-computed results for validation |
| `paper/` | AAAI paper LaTeX source |

## Environments

| Env | Modes | Description |
|-----|-------|-------------|
| 510K | SINGLE, STATIC, DYNAMIC, OBVIOUS | 4-player Chinese card game |
| Toy | HIDDEN, REVEALED | 2-action contextual bandit |
| Overcooked V3 | STATIC, DYNAMIC | Cooperative cooking (chef/waiter) |

## Algorithms

PPO (MaskablePPO), DQN, A2C, SAC, REINFORCE, MAPPO — tested across 3 environments with 100+ total seeds.

## Key Metric: kappa

**kappa** = gradient retention ratio (0 = full cancellation, 1 = full alignment). PG methods show kappa contraction under hidden info; value-based methods show reversed pattern.
