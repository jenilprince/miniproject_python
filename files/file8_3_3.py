import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv('football.csv')
#Pie chart
tot_goals_team=data.groupby(["Team"])["Goals"].sum()
print(tot_goals_team)
plt.pie(tot_goals_team.values,labels=tot_goals_team.index,autopct='%1.2f%%')
plt.title("Share of Total Goals by each Team")
plt.show()