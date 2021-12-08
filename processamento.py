#Importing stuff
import numpy as np
import pandas as pd

#Reading the dataset
logins = pd.read_parquet('logins.parquet5')
print(logins.head())