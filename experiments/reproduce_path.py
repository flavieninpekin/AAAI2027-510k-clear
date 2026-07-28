"""
Reproduce path integral analysis.

Usage:
    python experiments/reproduce_path.py
"""
import argparse, json
from pathlib import Path


def compute_all_path_integrals():
    """Compute path integrals for all 510K modes."""
    from iigc.eval import compute_path_integral

    modes = ["single", "static", "dynamic", "obvious"]
    results = {}
    for mode in modes:
        print(f"Computing path integral for {mode}...")
        result = compute_path_integral(
            model_dir=f"models_selfplay/{mode}",
            mode=mode,
            feature_dim=7,
            n_intervals=10,
        )
        results[mode] = result
        print(f"  {mode}: path = {result.get('path_length', 'N/A'):.4f}")

    # Save results
    out_path = Path("data/path_integral/path_results.json")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"Results saved to {out_path}")
    return results


if __name__ == "__main__":
    compute_all_path_integrals()
