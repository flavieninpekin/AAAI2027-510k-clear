def compute_irl(env_mode, n_episodes=1000, method="tabular"):
    """Run IRL to recover implicit reward weights."""
    from iigc.eval.irl import run_irl
    return run_irl(
        env_mode=env_mode,
        n_episodes=n_episodes,
        method=method,
    )
