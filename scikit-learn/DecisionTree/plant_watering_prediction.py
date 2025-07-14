import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
data = pd.DataFrame({
    'soil_moisture': [80, 30, 20, 60, 25, 40, 85, 50, 15, 90],
    'temperature':   [22, 35, 38, 28, 36, 30, 20, 27, 40, 19],
    'sunlight_hours': [4, 10, 9, 6, 11, 8, 3, 7, 12, 2],
    'is_wilting':     [0, 1, 1, 0, 1, 1, 0, 0, 1, 0],
    'needs_water':    [0, 1, 1, 0, 1, 1, 0, 0, 1, 0]  # 1 = Yes, needs water; 0 = No
})
X=data[['soil_moisture','temperature','sunlight_hours','is_wilting']]
y=data['needs_water']
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)
model=DecisionTreeClassifier(max_depth=4)
model.fit(X_train,y_train)

print("\n🌱 Plant Watering Assistant")
moisture = float(input("Enter soil moisture (%): "))
temp = float(input("Enter temperature (°C): "))
sunlight = float(input("Enter sunlight hours today: "))
wilting = int(input("Is the plant wilting? (1 = Yes, 0 = No): "))

user_input=pd.DataFrame([[moisture,temp,sunlight,wilting]], columns = X.columns)
prediction=model.predict(user_input)
print("💧 Your plant needs water!" if prediction[0]==1 else "✅ No watering needed right now.")
