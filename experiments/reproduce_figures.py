"""
Generate all paper figures from pre-computed data.

Usage:
    python experiments/reproduce_figures.py
"""
import argparse, subprocess, sys
from pathlib import Path


def generate_all_figures(data_dir="data", output_dir="figures_out"):
    """Generate all paper figures."""
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Try running the paper's figure generation script
    paper_gen = Path("paper/generate_figures.py")
    if paper_gen.exists():
        print("Generating figures using paper/generate_figures.py...")
        subprocess.run([sys.executable, str(paper_gen)], check=True)
    else:
        print(f"Warning: {paper_gen} not found, skipping figure generation")

    print(f"Figures output directory: {output_dir.resolve()}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-dir", default="data")
    parser.add_argument("--output-dir", default="figures_out")
    args = parser.parse_args()

    generate_all_figures(args.data_dir, args.output_dir)
