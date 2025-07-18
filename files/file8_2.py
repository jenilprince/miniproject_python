import pandas as pd
data=pd.read_csv('football.csv')
top_scorers=data.sort_values(by='Goals',ascending=False)
print(top_scorers.head(5))
most_assists=data.sort_values(by="Assists",ascending=False)
print(most_assists.head(1))
position_wise_avg=data.groupby(["Position"])["Goals"].mean()
print(position_wise_avg)
team_wise_total_goals = data.groupby(["Team"])["Goals"].sum()
print(team_wise_total_goals)