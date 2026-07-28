def train_dqn(mode="single", seed=42, total_timesteps=1_000_000, **kwargs):
    from .train_510k_dqn import main as _main
    import sys
    sys.argv = ["", f"--mode={mode}", f"--seed={seed}", f"--timesteps={total_timesteps}"]
    for k, v in kwargs.items():
        sys.argv.append(f"--{k}={v}")
    _main()


def train_dqn_all_seeds(mode="single", start_seed=41, n_seeds=8, timesteps=500_000):
    results = {}
    for i in range(n_seeds):
        seed = start_seed + i
        train_dqn(mode=mode, seed=seed, total_timesteps=timesteps)
        results[seed] = {"status": "done"}
    return results
