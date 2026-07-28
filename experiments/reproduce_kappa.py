"""
Reproduce kappa (gradient retention ratio) experiments.

Usage:
    python experiments/reproduce_kappa.py --all
    python experiments/reproduce_kappa.py --env 510k --algo ppo
"""
import argparse, json, sys
from pathlib import Path


def run_510k_ppo(mode="single", n_seeds=5, start_seed=41):
    """Train PPO and compute kappa for 510K."""
    from iigc.train import train_ppo_all_seeds
    train_ppo_all_seeds(mode=mode, start_seed=start_seed, n_seeds=n_seeds)


def run_510k_dqn(mode="single", n_seeds=8, start_seed=41):
    """Train DQN and compute kappa for 510K."""
    from iigc.train import train_dqn_all_seeds
    train_dqn_all_seeds(mode=mode, start_seed=start_seed, n_seeds=n_seeds)


def run_510k_a2c(mode="single", n_seeds=8, start_seed=41):
    """Train A2C and compute kappa for 510K."""
    from iigc.train import train_a2c
    for i in range(n_seeds):
        seed = start_seed + i
        print(f"[A2C {mode}] Seed {seed}")
        train_a2c(mode=mode, seed=seed)


def run_overcooked_v3(mode="static", n_seeds=8, start_seed=41):
    """Train PPO on Overcooked V3 and compute kappa."""
    from overcooked_adapt.train_v3 import train_parallel as _run
    _run(mode=mode, start_seed=start_seed, n_seeds=n_seeds)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--all", action="store_true")
    parser.add_argument("--env", choices=["510k", "overcooked", "toy"])
    parser.add_argument("--algo", choices=["ppo", "dqn", "a2c", "sac", "reinforce"])
    parser.add_argument("--mode", default=None)
    parser.add_argument("--seeds", type=int, default=None)
    args = parser.parse_args()

    if args.all:
        run_510k_ppo("single")
        run_510k_ppo("dynamic")
        run_510k_dqn("single")
        run_510k_dqn("dynamic")
        run_overcooked_v3("static")
        run_overcooked_v3("dynamic")
    else:
        print("Specify --all or --env + --algo")
