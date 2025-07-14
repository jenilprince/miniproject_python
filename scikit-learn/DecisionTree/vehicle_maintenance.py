import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
data = pd.DataFrame({
    'vehicle_age': [1, 5, 3, 8, 2, 10, 4, 7, 6, 9],
    'km_driven': [10000, 80000, 30000, 120000, 15000, 130000, 40000, 100000, 90000, 110000],
    'warning_lights': [0, 2, 0, 3, 0, 4, 1, 3, 2, 4],
    'engine_temp': [70, 95, 75, 105, 72, 110, 80, 100, 98, 108],
    'needs_service': [0, 1, 0, 1, 0, 1, 0, 1, 1, 1]  # 1 = Needs service, 0 = No service needed
})
X=data[['vehicle_age', 'km_driven', 'warning_lights', 'engine_temp']]
y=data['needs_service']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model=DecisionTreeClassifier(max_depth=4,random_state=42)
model.fit(X_train,y_train)
#
print("\n🚗 Vehicle Service Prediction")
vehicle_age = int(input("Enter vehicle age (years): "))
km = int(input("Enter kilometers driven: "))
lights = int(input("Enter number of warning lights on: "))
temp = float(input("Enter engine temperature (°C): "))

user_input=pd.DataFrame([[vehicle_age,km,lights,temp]], columns=X.columns)
prediction=model.predict(user_input)
print("Need Service" if prediction[0]==1 else "No Service")