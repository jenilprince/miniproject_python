from sklearn.linear_model import LinearRegression
import  pandas as pd
data=pd.DataFrame({'Num1':[1,2,3,4,5],'Num2':[1,2,3,4,5],'result':[2,4,6,8,10]})
model=LinearRegression()
model.fit(data[['Num1','Num2']],data['result'])
a=int(input("enter a number"))
b=int(input("enter another number"))
prediction=model.predict([[a,b]])


