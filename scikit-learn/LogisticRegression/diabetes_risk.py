from sklearn.linear_model import LogisticRegression
import pandas as pd
from sklearn.model_selection import train_test_split
data = pd.DataFrame({
    'Age':     [25, 35, 45, 55, 30, 50, 60, 40],
    'BMI':     [22.5, 27.0, 30.2, 33.1, 25.4, 28.0, 35.0, 29.5],
    'Glucose': [85, 90, 100, 130, 95, 120, 150, 110],
    'Risk':    [0, 0, 0, 1, 0, 1, 1, 1]  # 1 = High Risk
})
X=data[['Age','BMI','Glucose']]
y=data['Risk']
#split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)
#create
model=LogisticRegression()
#train
model.fit(X_train,y_train)
#predict
prediction=model.predict(pd.DataFrame({
    'Age': [43],
    'BMI': [22],
    'Glucose': [100]
}))
if prediction==1:
    print("Prediction: High Risk")
else:
    print("Prediction: Low Risk")
