import numpy as np
import pandas as pd
data=pd.read_csv('football.csv')
avg_goals=np.average(data["Goals"])
print(f"Average goals: {avg_goals}")
std_assists=np.std(data["Assists"])
print(f"Standard deviation of assists: {std_assists}")
mean=np.mean(data["Goals"])
for i in data["Goals"]:
    if i>mean:
        print(i)
goal_cont=np.sum(data["Goals"]+data["Assists"])
print(goal_cont)