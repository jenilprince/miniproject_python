from sklearn.tree import DecisionTreeClassifier
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
#Create data
data = pd.DataFrame({
    'age': [25, 45, 35, 23, 52, 40, 60, 30, 28, 50,25],
    'income': [25000, 70000, 50000, 20000, 100000, 65000, 120000, 45000, 30000, 85000,52000],
    'credit_score': [650, 800, 720, 600, 850, 780, 900, 710, 640, 830,786],
    'existing_debts': [1, 0, 0, 2, 0, 1, 0, 1, 2, 0,0],
    'loan_approved': [0, 1, 1, 0, 1, 1, 1, 1, 0, 1,1]  # 0 = No, 1 = Yes
})
X=data[['age','income','credit_score','existing_debts']]
y=data['loan_approved']
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
#
model=DecisionTreeClassifier(max_depth=4,random_state=42)
model.fit(X_train,y_train)
#
print("::LOAN PREDICTOR::")
age = int(input("Enter Age: "))
income = int(input("Enter Income: "))
credit = int(input("Enter Credit Score: "))
debts = int(input("Enter Number of Existing Debts: "))
#
user_input=pd.DataFrame([[age,income,credit,debts]],columns=X.columns)
prediction=model.predict(user_input)
print("Approved" if prediction==1 else "Not Approved")