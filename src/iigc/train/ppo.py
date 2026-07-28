def train_ppo_selfplay(
    mode="single",
    total_timesteps=1_000_000,
    seed=42,
    n_envs=8,
    log_dir="logs_selfplay",
    model_dir="models_selfplay",
    save_every=100_000,
):
    from .train_selfplay_parallel import train_seed_parallel
    return train_seed_parallel(
        mode=mode, seed=seed, total_timesteps=total_timesteps,
        n_envs=n_envs, log_dir=log_dir, model_dir=model_dir,
        save_every=save_every,
    )


def train_ppo_all_seeds(
    mode="single",
    start_seed=51,
    n_seeds=4,
    timesteps=1_000_000,
    n_envs=8,
    save_every=100_000,
):
    from .train_selfplay_parallel import train_all_parallel
    return train_all_parallel(
        mode=mode, start_seed=start_seed, n_seeds=n_seeds,
        timesteps=timesteps, n_envs=n_envs, save_every=save_every,
    )
