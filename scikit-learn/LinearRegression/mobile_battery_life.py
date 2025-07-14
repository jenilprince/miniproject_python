import pandas as pd
from sklearn.linear_model import LinearRegression
data = pd.DataFrame({
    'brightness': [80, 50, 100, 60],
    'app_usage': [5, 3, 6, 2],
    'network': [0, 1, 0, 1],
    'battery_life': [6, 10, 4, 11]
})
X=data[['brightness','app_usage','network']]
y=data['battery_life']
model=LinearRegression()
model.fit(X,y)

bright = float(input("Brightness (%): "))
apps = float(input("App usage (hours): "))
net = int(input("Network type (0 if Mobile data, 1 for Wi-Fi): "))

user_input=pd.DataFrame([[bright,apps,net]],columns=['brightness','app_usage','network'])
battery=model.predict(user_input)
print(f"Predicted Battery Life: {battery[0]:.2f} hours")