import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
data=pd.read_csv("data.csv")
print(data["Revenue"].groupby(data["Category"]).sum())
top=data["Units_Sold"].max()
print(f"Top units sold product: {top}")
order=data["Revenue"].groupby(data["Date"]).sum()
print(order.tail(1))
#Profit = Revenue - (Cost Price × Units Sold) (assume cost price as 80% of unit price)
data["Profit"]=data["Revenue"]-(data["Units_Sold"]*data["Unit_Price"]*.8)
print(data)