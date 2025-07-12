from sklearn.linear_model import LogisticRegression
import pandas as pd
from sklearn.model_selection import train_test_split
data = pd.DataFrame({
    'Income':       [30000, 40000, 35000, 45000, 50000, 60000, 65000, 70000],
    'Credit_Score': [580, 620, 600, 640, 680, 700, 720, 750],
    'Loan_Amount':  [10000, 12000, 11000, 14000, 13000, 16000, 17000, 18000],
    'Approved':     [0, 0, 0, 1, 1, 1, 1, 1]
})
X=data[['Income', 'Credit_Score', 'Loan_Amount']]
y=data['Approved']
#input
inc=int(input("Enter the amount of income: "))
credit=int(input("Enter your credit score: "))
loan = int(input("Enter the loan amount: "))
#split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)
#create
model=LogisticRegression()
#train
model.fit(X_train,y_train)
#predict
prediction=model.predict(pd.DataFrame({
    'Income': [inc],
    'Credit_Score': [credit],
    'Loan_Amount': [loan],
}))
if prediction==1:
    print("Approved")
else:
    print("Not Approved")
