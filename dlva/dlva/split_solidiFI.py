import pandas as pd

df = pd.read_csv("SolidiFI_benchmark.csv")
n = len(df)
chunk_size = 30  # around 4 chunks for 444 rows

print("Total rows:", n)
part = 1
for start in range(0, n, chunk_size):
    end = min(start + chunk_size, n)
    out = f"SolidiFI_benchmark_part{part}.csv"
    df.iloc[start:end].to_csv(out, index=False)
    print(out, "rows:", end - start)
    part += 1
