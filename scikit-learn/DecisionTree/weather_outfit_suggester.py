import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

data = pd.DataFrame({
    'temperature': [30, 22, 10, 5, 15, 25, 12, 8, 28, 18],
    'wind_speed': [5, 10, 20, 25, 15, 8, 18, 22, 6, 12],
    'humidity': [40, 50, 60, 80, 55, 45, 70, 85, 38, 65],
    'is_raining': [0, 0, 1, 1, 0, 0, 1, 1, 0, 1],
    'wear_warm_clothes': [0, 0, 1, 1, 1, 0, 1, 1, 0, 1]  # 1 = Warm clothes, 0 = Light clothes
})
X=data[['temperature', 'wind_speed', 'humidity', 'is_raining']]
y=data['wear_warm_clothes']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = DecisionTreeClassifier(max_depth=4)
model.fit(X_train, y_train)
#input
print("\n👕 Outfit Suggestion:")
temp = float(input("Enter temperature (°C): "))
wind = float(input("Enter wind speed (km/h): "))
humidity = float(input("Enter humidity (%): "))
rain = int(input("Is it raining? (1 = Yes, 0 = No): "))

user_input=pd.DataFrame([[temp,wind,humidity,rain]], columns=X.columns)
prediction=model.predict(user_input)
print("🧥 Wear warm clothes!" if prediction[0]==1 else "👕 Light clothes are enough!")
