import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

# Step 1: Sample synthetic dataset
def disease_check(fever,cough,fatigue,age):
    data = pd.DataFrame({
        'fever': [101.5, 99.0, 102.3, 98.6, 100.5, 103.1, 97.5, 104.0, 98.0, 102.8],
        'cough': [8, 2, 9, 1, 6, 10, 0, 9, 1, 8],
        'fatigue': [7, 1, 8, 0, 5, 9, 0, 10, 1, 8],
        'age': [25, 40, 35, 22, 30, 50, 18, 65, 28, 45],
        'disease': [1, 0, 1, 0, 1, 1, 0, 1, 0, 1]  # 1 = Positive, 0 = Negative
    })
    X=data[['fever','cough','fatigue','age']]
    y=data['disease']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model=DecisionTreeClassifier(max_depth=4,random_state=42)
    model.fit(X_train,y_train)
    #
    user_data=pd.DataFrame([[fever,cough,fatigue,age]],columns=X.columns)
    prediction=model.predict(user_data)
    print("Positive" if prediction[0]==1 else "Negative")
print("\n🔍 Disease Diagnosis Predictor")
fever = float(input("Enter body temperature (°F): "))
cough = int(input("Cough severity (0 to 10): "))
fatigue = int(input("Fatigue level (0 to 10): "))
age = int(input("Age: "))
disease_check(fever,cough,fatigue,age)