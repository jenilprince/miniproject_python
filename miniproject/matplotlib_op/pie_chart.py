import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
data=pd.read_csv("../data.csv")
plt.figure(figsize=[8,8])
ordered=data.groupby("Product")["Revenue"].sum()
print(ordered)
plt.pie(ordered,labels=ordered.index,autopct="%1.2f%%")
plt.show()

