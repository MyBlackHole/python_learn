import pandas as pd
from io import BytesIO


with open("linux.csv", "rb") as f:
    b = f.read()

nio = BytesIO(b)
df = pd.read_csv(nio)
nio.close()
print(df)
