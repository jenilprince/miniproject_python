from sklearn.linear_model import LogisticRegression
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
data = pd.read_csv("data.csv", usecols=['text', 'label_num'])
data.columns = ['Text', 'Label']  # Rename for clarity
X=data['Text']
y=data['Label']
#split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=.2,random_state=46)
#Vectoriser - converts text to numbers
vectorizer=TfidfVectorizer()
vectorized_data=vectorizer.fit_transform(X_train)
vectorized_test=vectorizer.transform(X_test)
#create
model=LogisticRegression()
#train
model.fit(vectorized_data,y_train)
#Test
test_msg=[input("Enter a message: ")]
#convert to vector
test_vector=vectorizer.transform(test_msg)
prediction=model.predict(test_vector)
if prediction==1:
    print("Spam")
else:
    print("Not Spam")
