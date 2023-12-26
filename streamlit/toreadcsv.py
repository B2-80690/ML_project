import numpy as np
import pandas as pd

data = pd.read_csv("movieData2.csv")
df = pd.DataFrame(data)
print(df.head(5))
