def compute_path_integral(model_dir, mode, feature_dim=7, n_intervals=10):
    """Compute path integral (cumulative L2 distance through feature space)."""
    from iigc.eval.path_integral import compute_path as _compute
    return _compute(
        model_dir=model_dir,
        mode=mode,
        feature_dim=feature_dim,
        n_intervals=n_intervals,
    )
