import importlib.util
import sys
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    import pandas as pd


def check_import(pack: list[str]) -> bool:
    """
    Try to import a package and return True if available.
    Returns False if the package is not installed.
    """
    check = True
    print("LOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")
    for p in pack:
        res = importlib.util.find_spec(p)
        if res:
            pack_name = importlib.import_module(p)
            ver = pack_name.__version__
            print(f"[OK] {p} ({ver})")
        else:
            print(f"{p} is not installed")
            check = False
    return check


def generate_visualization(graph: "pd.DataFrame", png_name: str) -> None:
    """Generate simulated Matrix data using numpy."""
    import matplotlib.pyplot as mp
    try:
        mp.figure(figsize=(10, 6))
        mp.plot(graph['timestamp'], graph['signal'])
        mp.title('Matrix_analysis.png')
        mp.savefig(png_name)
    except Exception as error:
        print(f"an error has been aquired {error}")
        sys.exit(1)


def generate_data() -> "pd.DataFrame":
    import numpy as np
    import pandas as pn
    print("\nAnalyzing Matrix data...")
    data = {
        'signal': np.random.randn(1000),
        'noise': np.random.randn(1000),
        'timestamp': np.arange(1000)
    }
    print(f"Processing {len(data['signal'])} data points...")
    gr = pn.DataFrame(data)
    return gr


if __name__ == "__main__":
    pack = ['pandas', 'numpy', 'matplotlib']
    png_name = 'matrix_analysis.png'
    if check_import(pack):
        res = generate_data()
        print('Generating visualization...\n')
        generate_visualization(res, png_name)
        print("\nAnalysis complete!")
        print("Results saved to: matrix_analysis.png")
    else:
        print("\nPlease install missing dependencies and try again.")
        print("With pip:    pip install -r requirements.txt")
        print("With Poetry: poetry install")
