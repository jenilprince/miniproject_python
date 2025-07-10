import numpy_op as np
import matplotlib.pyplot as plt
import pandas as pd
data=pd.read_csv("data.csv")
print(data.head())
print(data.isnull().sum())
print(data.describe())
