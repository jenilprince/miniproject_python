import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
data=pd.read_csv("../data.csv")
plt.plot(data["Date"],data["Revenue"],color="green",linestyle="-",label="Revenue")
plt.legend(loc="best")
plt.grid(True)
plt.xlabel("Date")
plt.ylabel("Revenue")
plt.title("Daily Revenue Trend")
plt.show()