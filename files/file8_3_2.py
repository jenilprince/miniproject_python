import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv('football.csv')
#Line chart
plt.plot(data['player'],data["Matches_Played"],color="red",linestyle="--",marker="o",label="Matches Played")
plt.plot(data["Goals"],color="blue",linestyle="--",marker="*",label="Goals")
plt.xlabel("Player")
plt.legend()
plt.grid(True)
plt.show()
