import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
# Step 1: Create dataset
data = pd.DataFrame({
    'age': [25, 45, 38, 29, 50, 31, 40, 28, 35, 42],
    'salary': [30000, 80000, 60000, 35000, 95000, 40000, 70000, 33000, 55000, 78000],
    'years_at_company': [1, 10, 5, 2, 12, 3, 8, 1, 4, 9],
    'job_satisfaction': [4, 8, 7, 3, 9, 5, 6, 2, 6, 7],
    'attrition': [1, 0, 0, 1, 0, 1, 0, 1, 0, 0]  # 1 = Left, 0 = Stayed
})
X=data[['age','salary','years_at_company','job_satisfaction']]
y=data['attrition']
#
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
#
model=DecisionTreeClassifier(max_depth=4,random_state=42)
model.fit(X_train,y_train)
#
##user input
age=int(input("Enter age: "))
salary=int(input("Enter salary: "))
years=int(input("Enter years at company: "))
job_satisfaction=int(input("Enter job satisfaction(1 to 10): "))
#
input_data=pd.DataFrame([[age,salary,years,job_satisfaction]],columns=X.columns)
prediction=model.predict(input_data)
print("Left" if prediction[0]==1 else "Stayed")