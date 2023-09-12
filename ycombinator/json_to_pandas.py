'''
Conver the companies.json file to .csv
'''

import pandas as pd

df = pd.read_json('./companies.json')

df_transposed = df.transpose()

# Set one of the keys as the index (e.g., "name" in this example)
df_transposed = df_transposed.set_index("name")

df_transposed.to_csv("./companies.csv")