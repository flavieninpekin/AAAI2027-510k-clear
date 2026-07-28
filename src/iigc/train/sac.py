def train_sac(mode="single", seed=42, total_timesteps=1_000_000, **kwargs):
    from .train_510k_sac import main as _main
    import sys
    sys.argv = ["", f"--mode={mode}", f"--seed={seed}", f"--timesteps={total_timesteps}"]
    for k, v in kwargs.items():
        sys.argv.append(f"--{k}={v}")
    _main()
