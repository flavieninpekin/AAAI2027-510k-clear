def train_reinforce(mode="single", seed=42, total_timesteps=500_000, **kwargs):
    from .train_510k_reinforce import main as _main
    import sys
    sys.argv = ["", f"--mode={mode}", f"--seed={seed}", f"--timesteps={total_timesteps}"]
    for k, v in kwargs.items():
        sys.argv.append(f"--{k}={v}")
    _main()


def train_reinforce_sp(mode="single", seed=42, total_timesteps=500_000, **kwargs):
    from .train_reinforce_sp import main as _main
    import sys
    sys.argv = ["", f"--mode={mode}", f"--seed={seed}", f"--timesteps={total_timesteps}"]
    for k, v in kwargs.items():
        sys.argv.append(f"--{k}={v}")
    _main()
