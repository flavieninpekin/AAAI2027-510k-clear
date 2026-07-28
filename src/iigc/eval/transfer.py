def evaluate_transfer(policy_path, modes=None):
    """Evaluate a frozen policy across different rule modes."""
    from iigc.eval.transfer import run_transfer
    if modes is None:
        modes = ["single", "static", "dynamic"]
    return run_transfer(policy_path=policy_path, target_modes=modes)
