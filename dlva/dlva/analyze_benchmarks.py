import glob
import os
import pandas as pd


def summarize_file(path: str):
    name = os.path.basename(path)
    print("=" * 80)
    print(f"Summary for {name}")
    print("=" * 80)

    df = pd.read_csv(path)
    print("Total contracts:", len(df))
    print("Columns:", list(df.columns))

    # Treat numeric columns as possible vulnerability flags
    numeric_cols = [
        c for c in df.columns
        if df[c].dtype != "object" and c.lower() not in ("id", "index")
    ]

    print("\nVulnerability flag counts (sum over numeric columns):")
    for col in numeric_cols:
        try:
            s = df[col].sum()
            print(f"  {col}: {int(s)} positives")
        except Exception:
            pass

    print("\n")


if __name__ == "__main__":
    # Loop over all DLVA prediction CSVs in this folder
    for path in sorted(glob.glob("DLVA_Predictions_for_*.csv")):
        summarize_file(path)
