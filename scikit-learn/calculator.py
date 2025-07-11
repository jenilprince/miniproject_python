from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd
data_add=pd.DataFrame({
    'Number1': [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],
    'Number2': [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16],
    'Result': [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]
})
a=int(input("Enter a number: "))
b=int(input("Enter another number: "))
##create
model=LinearRegression()
model.fit(data_add[['Number1','Number2']],data_add['Result'])
prediction = model.predict(pd.DataFrame({'Number1': [a], 'Number2': [b]}))
print(f"{prediction[0].item():.2f}")
