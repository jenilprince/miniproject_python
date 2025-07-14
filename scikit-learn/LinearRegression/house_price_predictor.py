import pandas as pd
from sklearn.linear_model import LinearRegression

# Sample Data
data = pd.DataFrame({
    'area': [1000, 1500, 2000, 1800],
    'bedrooms': [2, 3, 4, 3],
    'bathrooms': [1, 2, 3, 2],
    'age': [10, 5, 2, 3],
    'price': [40, 60, 80, 70]
})
X=data[['area','bedrooms','bathrooms','age']]
y=data['price']
model=LinearRegression()
model.fit(X,y)

area = int(input("Enter area (sq.ft): "))
bedrooms = int(input("Enter number of bedrooms: "))
bathrooms = int(input("Enter number of bathrooms: "))
age = int(input("Enter age of house: "))

input_pred=pd.DataFrame([[area,bedrooms,bathrooms,age]],columns=['area','bedrooms','bathrooms','age'])
prediction=model.predict(input_pred)

print(f"Predicted price: ₹{prediction[0]:.2f} Lakhs")