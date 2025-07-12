from sklearn.linear_model import LogisticRegression
import numpy as np
from sklearn.model_selection import train_test_split
import pandas as pd
data = pd.DataFrame({
    'Hours': [0,1,2,3,4,5,6,7,8,9,10],
    'Pass': [0,0,0,0,0,1,1,1,1,1,1]
})
X=data[['Hours']]
y=data['Pass']
#split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3)
#create
model=LogisticRegression()
#train
model.fit(X_train,y_train)
#make predictions
prediction=model.predict(pd.DataFrame({'Hours': [4.3]}))
if prediction==1:
    print("Prediction: Pass")

else:
    print("Prediction: Fail")