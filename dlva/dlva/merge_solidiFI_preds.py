import glob
import pandas as pd

files = sorted(glob.glob("DLVA_Predictions_for_SolidiFI_benchmark_part*.csv"))
print("Merging files:", files)

dfs = [pd.read_csv(f) for f in files]
merged = pd.concat(dfs, ignore_index=True)
print("Total rows merged:", len(merged))

merged.to_csv("DLVA_Predictions_for_SolidiFI_benchmark.csv", index=False)
print("Wrote DLVA_Predictions_for_SolidiFI_benchmark.csv")
