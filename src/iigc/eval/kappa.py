def compute_kappa(policy_path, mode="single", n_episodes=50, device="cpu"):
    """Compute kappa (gradient retention ratio) for a trained policy."""
    from iigc.eval.eval_ppo_kappa import compute_kappa_on_policy
    import torch
    return compute_kappa_on_policy(
        policy_path=policy_path,
        mode=mode,
        n_episodes=n_episodes,
        device=torch.device(device),
    )
