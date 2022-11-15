import time

from pyarrow import csv

def load_by_arrow(filePath):
    # API :https://arrow.apache.org/docs/python/generated/pyarrow.csv.read_csv.html
    table = csv.read_csv(filePath)
    
    return table.to_pandas()

import pandas as pd

def load_by_pandas(filePath):
    df = pd.read_csv(filePath)
    
    return df
    

if __name__ == "__main__":  
    filePath = 'workdf.csv'
        
    start = time.time()
    pa_df = load_by_arrow(filePath)
    end = time.time()
    print(end-start)
    
    start = time.time()
    pd_df = load_by_pandas(filePath)
    end = time.time()
    print(end-start)
