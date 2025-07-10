import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# FOR READING CSV FILE
data=pd.read_csv("data.csv")
# TO FIND MEAN
mean=np.mean(data["Units_Sold"])
print(f"Mean Sold: {mean}")
# TO FIND STANDARD DEVIATION
std=np.std(data["Revenue"])
print(f"Standard Deviation of Revenue: {std}")
# TO FIND TOTAL REVENUE
tot=np.sum(data["Units_Sold"]*data["Unit_Price"])
print(f"Total Revenue: {tot}")
# TO FIND HIGHEST REVENUE IN A DAY
arr=np.sort(data["Revenue"])
print(f"Highest Revenue in a day: {arr[-1]}")


