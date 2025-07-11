import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np
data = pd.DataFrame({
    'Age_Months': [6, 12, 18, 24, 6, 12, 18, 24],
    'RAM_GB':     [4, 4, 6, 6, 8, 8, 6, 4],
    'Storage_GB': [64, 128, 64, 128, 128, 256, 256, 64],
    'Brand_Code': [1, 1, 2, 2, 3, 3, 2, 1],  # 1: Samsung, 2: Redmi, 3: iPhone
    'Price':      [15000, 14000, 13000, 12000, 35000, 34000, 25000, 11000]
})
age=int(input("Enter the age in months: "))
ram = int(input("Enter the RAM in GB: "))
storage = int(input("Enter the storage in GB: "))
brand = int(input("Enter the brand code (1 for Samsung, 2 for Redmi, 3 for iPhone): "))
model = LinearRegression()
model.fit(data[['Age_Months', 'RAM_GB', 'Storage_GB', 'Brand_Code']], data['Price'])
prediction=model.predict(pd.DataFrame({'Age_Months': [age], 'RAM_GB': [ram], 'Storage_GB': [storage], 'Brand_Code': [brand]}))
print(f"₹{prediction[0]:.2f} only")