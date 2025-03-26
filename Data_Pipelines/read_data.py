from google.colab import files

uploaded = files.upload()  # Opens file upload dialog

import pandas as pd

df = pd.read_parquet("yellow_tripdata_2025-01.parquet")  # For Parquet files
print(df.head())