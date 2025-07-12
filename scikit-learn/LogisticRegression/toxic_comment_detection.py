from sklearn.linear_model import LogisticRegression
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
data = {
    'Text': [
        "You're a complete failure", "Thanks a lot for your help", "Nobody likes you", "Appreciate your kindness",
        "You're the worst", "Great explanation", "Get lost", "Very informative", "Shut up already", "I love your work",
        "You're dumb", "Well done!", "I hate everything you say", "Thank you for the support",
        "You're pathetic", "Nice effort", "You're a joke", "Helpful content", "Disgusting attitude", "Good example",
        "You should quit", "That's a clever idea", "Your opinion is trash", "Respectful and clear", "Annoying as always",
        "Nicely written", "You're so annoying", "Thanks for sharing", "Nobody wants your opinion", "Clear and simple",
        "You're an embarrassment", "Great advice", "Keep your mouth shut", "Good effort", "Such stupidity", "Explained well",
        "You're a piece of trash", "Appreciate the details", "Go to hell", "Thanks for your time",
        "Why do you even try?", "Very helpful post", "You ruined everything", "Brilliant example",
        "I can't stand you", "Much appreciated", "Your work is garbage", "Excellent feedback",
        "You talk nonsense", "Very professional", "You're sick", "Nice and polite", "I despise you", "Respectful message",
        "You're not welcome here", "I value your opinion", "Pathetic excuse", "Useful reply", "So irritating", "Nicely explained",
        "You're disgusting", "Very well done", "You smell like trash", "Thanks, that helped a lot",
        "Stupid question", "Nice question!", "You're nothing", "I learned something new",
        "Such a waste", "Highly informative", "Nobody cares about you", "Awesome tips",
        "Don't talk ever again", "That clarified things", "What a fool", "Thanks for the clarity",
        "Idiot", "Very courteous", "Don't waste space", "Super detailed", "I hate this", "Love this!",
        "Total nonsense", "Very neat", "This is dumb", "This was so helpful", "You're evil", "Awesome suggestion",
        "Worst post ever", "Makes perfect sense", "Foolish message", "Thanks for the update",
        "Disrespectful garbage", "Kind words", "Terrible reply", "Very respectful", "Waste of space", "Very nice of you",
        "Ugly thoughts", "Helpful reply"
    ],
    'Label': [1, 0, 1, 0, 1, 0, 1, 0, 1, 0,
        1, 0, 1, 0, 1, 0, 1, 0, 1, 0,
        1, 0, 1, 0, 1, 0, 1, 0, 1, 0,
        1, 0, 1, 0, 1, 0, 1, 0, 1, 0,
        1, 0, 1, 0, 1, 0, 1, 0, 1, 0,
        1, 0, 1, 0, 1, 0, 1, 0, 1, 0,
        1, 0, 1, 0, 1, 0, 1, 0, 1, 0,
        1, 0, 1, 0, 1, 0, 1, 0, 1, 0,
        1, 0, 1, 0, 1, 0, 1, 0, 1, 0,
        1, 0, 1, 0, 1, 0, 1, 0, 1, 0,]
}
X=data['Text']
y=data['Label']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
vect=TfidfVectorizer()
X_vec=vect.fit_transform(X_train)
X_testv=vect.transform(X_test)
model=LogisticRegression()
model.fit(X_vec,y_train)
test_data=[input("Enter comment: ")]
test_vec=vect.transform(test_data)
pred=model.predict(test_vec)
print("Positive" if pred[0]==0 else "Toxic")


