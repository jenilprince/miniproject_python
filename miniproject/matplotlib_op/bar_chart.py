import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
data=pd.read_csv("../data.csv")
plt.bar(data["Category"],data["Revenue"],color="skyblue",label="Graph",width=0.5)
plt.title("Revenue by Category")
plt.xlabel("Category")
plt.ylabel("Revenue")
plt.grid(True)
plt.legend(loc="best")
plt.show()