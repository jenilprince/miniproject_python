import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
data = pd.DataFrame({
    'num_links': [0, 5, 1, 8, 0, 4, 2, 7, 1, 6],
    'num_caps': [3, 50, 10, 70, 1, 40, 5, 60, 7, 55],
    'has_buy_now': [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    'email_length': [100, 250, 180, 300, 90, 230, 120, 280, 130, 260],
    'spam': [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]  # 1 = Spam, 0 = Not Spam
})
X=data[['num_links', 'num_caps', 'has_buy_now', 'email_length']]
y=data['spam']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model=DecisionTreeClassifier(max_depth=4,random_state=42)
model.fit(X_train,y_train)

# Step 6: Try with Real Input
print("\n📧 Test your own email")
num_links = int(input("Number of links: "))
num_caps = int(input("Number of capital letters: "))
has_buy_now = int(input("Contains 'buy now' or 'free'? (1 = Yes, 0 = No): "))
length = int(input("Length of email: "))

user_input=pd.DataFrame([[num_links,num_caps,has_buy_now,length]],columns=X.columns)
prediction=model.predict(user_input)
print("Spam" if prediction[0]==1 else "Not Spam")