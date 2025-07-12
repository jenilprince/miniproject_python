from sklearn.linear_model import LogisticRegression
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
data = pd.DataFrame({
    'Text': [
        "The teacher explains well",              # Positive
        "Too many assignments",                   # Negative
        "Helpful and friendly",                   # Positive
        "Class is boring",                        # Negative
        "Great teaching style",                   # Positive
        "I don't understand anything",            # Negative
        "Very engaging sessions",                 # Positive
        "The lectures are hard to follow",        # Negative
        "Always available for doubts",            # Positive
        "Too fast, can’t keep up",                # Negative
        "Makes learning fun",                     # Positive
        "Slides are confusing",                   # Negative
        "Gives good real-life examples",          # Positive
        "Not interested in students' questions",  # Negative
        "Explains with patience",                 # Positive
        "Very disorganized class",                # Negative
        "Motivates the students",                 # Positive
        "Often arrives late",                     # Negative
        "Provides useful feedback",               # Positive
        "Homework is too difficult",              # Negative
        "Supports us during exams",               # Positive
        "Rude behavior in class",                 # Negative
        "Creates a positive learning atmosphere", # Positive
        "Never responds to emails",               # Negative
        "Explains topics multiple times",         # Positive
        "Focuses too much on theory",             # Negative
        "Encourages class participation",         # Positive
        "Assignments are unclear",                # Negative
        "Interactive and fun",                    # Positive
        "Test questions not from syllabus",        # Negative
        "Bad",
        "Good","Worst"
    ],
    'Label': [
        1, 0, 1, 0, 1, 0,
        1, 0, 1, 0, 1, 0,
        1, 0, 1, 0, 1, 0,
        1, 0, 1, 0, 1, 0,
        1, 0, 1, 0, 1, 0, 0, 1, 0
    ]
})
X=data["Text"]
y=data['Label']
#split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
#vectorise
vectorizer=TfidfVectorizer()
X_vectorized=vectorizer.fit_transform(X_train)
test_vectorized=vectorizer.transform(X_test)
#create
model=LogisticRegression()
#train
model.fit(X_vectorized,y_train)
#new data
test_data=[input("Enter student review: ")]
#to vector
test_vector=vectorizer.transform(test_data)
test_pred=model.predict(test_vector)
print("Positive " if test_pred == 1 else "Negative ")