import pandas as pd

# Load only first few rows for preview
df = pd.read_csv("data/large_data.csv", nrows=10)

# Save to image
import dataframe_image as dfi
dfi.export(df, 'dataset_preview.png')

