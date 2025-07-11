import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
# Mark predictor based on number of hours studied
## Create data
data=pd.DataFrame({
    'Hours': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Marks': [5, 10, 20, 25, 40, 45, 50, 65, 70, 85, 95]
})
## Give new variables to data individuals
X=data[['Hours']]# input
y=data[['Marks']]# output
## Create new model
model=LinearRegression()
#Train the model
model.fit(X,y)
#Make predictions
model.predict(X)
## Make it predict new output from the input we give
num=int(input("Enter the number of hours studied: "))
if num<0:
    print("Sorry, the number of hours is not valid")
else:
    test_hours = pd.DataFrame({'Hours': [num]})
    test_prediction=model.predict(test_hours)
    marks=test_prediction[0].item()
    capped=max(0,min(marks,100))
    print(f"Prediction marks: {capped:.4f}")

