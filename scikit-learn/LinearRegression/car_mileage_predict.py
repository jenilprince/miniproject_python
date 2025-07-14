import pandas as pd
from sklearn.linear_model import LinearRegression
data = pd.DataFrame({
    'engine': [1200, 1500, 1000, 1600],
    'weight': [900, 1100, 800, 1200],
    'age': [2, 4, 1, 6],
    'mileage': [18, 15, 22, 12]
})
X=data[['engine','weight','age']]
y=data['mileage']
model=LinearRegression()
model.fit(X,y)

engine = int(input("Enter engine size (cc): "))
weight = int(input("Enter car weight (kg): "))
age = int(input("Enter age of car (years): "))

userinp=pd.DataFrame([[engine,weight,age]],columns=['engine','weight','age'])
prediction=model.predict(userinp)
print(f"Predicted Mileage: {prediction[0]:.2f} km/l")