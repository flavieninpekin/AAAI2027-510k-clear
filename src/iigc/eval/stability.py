def compute_stability(results_dir="data/path_integral"):
    """Generate stability maps (path length vs curvature)."""
    from iigc.eval.stability_map_v2 import main as _main
    return _main(results_dir)
