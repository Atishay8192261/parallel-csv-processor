import pandas as pd
import numpy as np
import time

start = time.time()

rows = 10_000_000

print(f"Generating {rows:,} rows...")

df = pd.DataFrame({
    'id': np.arange(1, rows + 1),
    'value1': np.random.rand(rows) * 100,
    'value2': np.random.normal(loc=50, scale=15, size=rows),
    'category': np.random.choice(['X', 'Y', 'Z'], size=rows),
    'flag': np.random.choice([0, 1], size=rows),
    'score': np.random.randint(1, 100, size=rows)
})

print("Saving to data/large_data.csv...")
df.to_csv('data/large_data.csv', index=False)

end = time.time()
print(f"Time taken: {end - start:.2f} seconds")

