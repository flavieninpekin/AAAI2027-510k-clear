"""
One-click reproduction of all paper results.

Usage:
    python experiments/reproduce_all.py          # Full reproduction (slow)
    python experiments/reproduce_all.py --quick  # Quick sanity check
"""
import argparse, subprocess, sys, time


def run_script(name, args=None):
    """Run a reproduction script."""
    cmd = [sys.executable, f"experiments/{name}"]
    if args:
        cmd.extend(args)
    print(f"\n{'='*60}")
    print(f"Running: {' '.join(cmd)}")
    print(f"{'='*60}")
    t0 = time.time()
    result = subprocess.run(cmd)
    elapsed = time.time() - t0
    print(f"Finished in {elapsed:.0f}s ({elapsed/60:.1f} min)")
    return result.returncode


def reproduce_all(quick=False):
    """Run all experiments."""
    if quick:
        print("Quick mode: running minimal seeds")
        # Just compute kappa on pre-trained models if available
        run_script("reproduce_kappa.py", ["--env", "overcooked", "--algo", "ppo"])
    else:
        # Full reproduction
        # Phase 1: Kappa experiments (requires training)
        run_script("reproduce_kappa.py", ["--all"])

        # Phase 2: Path integral analysis
        run_script("reproduce_path.py")

    # Phase 3: Generate figures
    run_script("reproduce_figures.py")

    print("\nAll done!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--quick", action="store_true", help="Quick sanity check")
    args = parser.parse_args()

    reproduce_all(quick=args.quick)
