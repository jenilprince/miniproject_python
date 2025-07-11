import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv('football.csv')
# BAR CHART
top_five=data.sort_values(by="Goals",ascending=False)[0:5]
print(top_five["player"])
plt.bar(top_five["player"],top_five["Goals"],color='skyblue',label="Goals")
plt.title("Top Goal Scorers")
plt.grid(True)
plt.legend(loc="best")
plt.show()