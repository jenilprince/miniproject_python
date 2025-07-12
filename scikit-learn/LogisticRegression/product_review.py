from sklearn.linear_model import LogisticRegression
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
data = pd.DataFrame({
    'Text': [
        "Loved the product, highly recommended!",      # 1
        "Very poor quality, not satisfied",            # 2
        "Excellent, works as described",               # 3
        "Stopped working in a week",                   # 4
        "Good value for money",                        # 5
        "Worst experience ever",                       # 6
        "Completely satisfied with the purchase",      # 7
        "Broke after one use",                         # 8
        "Amazing features and easy to use",            # 9
        "Not worth the price",                         # 10
        "Super fast delivery",                         # 11
        "Terrible packaging",                          # 12
        "Quality is top-notch",                        # 13
        "Doesn't match the description",               # 14
        "Absolutely love it",                          # 15
        "Very disappointed",                           # 16
        "Great quality and design",                    # 17
        "Feels cheap and flimsy",                      # 18
        "Five stars, will buy again",                  # 19
        "Save your money, avoid this",                 # 20
        "Really useful and affordable",                # 21
        "Does not work as promised",                   # 22
        "Highly efficient and compact",                # 23
        "Arrived broken",                              # 24
        "Looks great and works well",                  # 25
        "Poor customer support",                       # 26
        "Perfect for my needs",                        # 27
        "Waste of money",                              # 28
        "Very durable and reliable",                   # 29
        "Functionality is bad",                        # 30
        "Pleasantly surprised",                        # 31
        "Wouldn’t recommend",                          # 32
        "Met all my expectations",                     # 33
        "It’s just okay",                              # 34
        "Awesome product!",                            # 35
        "Bad smell, unusable",                         # 36
        "Truly a lifesaver",                           # 37
        "Not as advertised",                           # 38
        "Reliable and well-built",                     # 39
        "Too noisy",                                   # 40
        "User-friendly interface",                     # 41
        "Very slow performance",                       # 42
        "Perfect size and shape",                      # 43
        "Didn't work on arrival",                      # 44
        "Works like a charm",                          # 45
        "It’s a scam",                                 # 46
        "Satisfied with the service",                  # 47
        "Misleading details",                          # 48
        "Top quality and excellent value",             # 49
        "Horrible experience",                         # 50
        "Exactly what I needed",                       # 51
        "Broken on delivery",                          # 52
        "Premium build, looks amazing",                # 53
        "Feels very cheap",                            # 54
        "No complaints at all",                        # 55
        "Died within days",                            # 56
        "Well packaged and quick delivery",            # 57
        "Overheats quickly",                           # 58
        "Would buy again",                             # 59
        "Doesn't fit properly",                        # 60
        "Super happy with this",                       # 61
        "Pain to use",                                 # 62
        "Highly recommended by my friends",            # 63
        "Unusable after a week",                       # 64
        "Just perfect!",                               # 65
        "Does not meet expectations",                  # 66
        "Better than I thought",                       # 67
        "Looks used",                                  # 68
        "Exceptional product",                         # 69
        "Poor battery life",                           # 70
        "Everything works perfectly",                  # 71
        "Not durable at all",                          # 72
        "So glad I bought this",                       # 73
        "Doesn’t connect properly",                    # 74
        "Exceeded my expectations",                    # 75
        "Color faded quickly",                         # 76
        "Love the way it works",                       # 77
        "Faulty buttons",                              # 78
        "Really great experience",                     # 79
        "Not user-friendly",                           # 80
        "Awesome for everyday use",                    # 81
        "Couldn’t use it",                             # 82
        "Smart and elegant",                           # 83
        "Total disappointment",                        # 84
        "Easy to set up",                              # 85
        "Returned it immediately",                     # 86
        "10/10 would recommend",                       # 87
        "Very fragile",                                # 88
        "Superb quality",                              # 89
        "Useless instructions",                        # 90
        "Amazing experience overall",                  # 91
        "Didn't meet the description",                 # 92
        "Better than most products",                   # 93
        "Buttons stopped working",                     # 94
        "Extremely happy with this",                   # 95
        "Packaging was damaged",                       # 96
        "Exactly as advertised",                       # 97
        "Not what I ordered",                          # 98
        "Best purchase I’ve made",                     # 99
        "Stopped working suddenly",                     # 100
        "Nice",
        "Very nice",
        "Very good",
        "Very bad",
        "Failure",
        "Best product",
        "Beautiful",
        "Well, it works... sometimes."
    ],
    'Label': [
        1, 0, 1, 0, 1,
        0, 1, 0, 1, 0,
        1, 0, 1, 0, 1,
        0, 1, 0, 1, 0,
        1, 0, 1, 0, 1,
        0, 1, 0, 1, 0,
        1, 0, 1, 0, 1,
        0, 1, 0, 1, 0,
        1, 0, 1, 0, 1,
        0, 1, 0, 1, 0,
        1, 0, 1, 0, 1,
        0, 1, 0, 1, 0,
        1, 0, 1, 0, 1,
        0, 1, 0, 1, 0,
        1, 0, 1, 0, 1,
        0, 1, 0, 1, 0,
        1, 0, 1, 0, 1,
        0, 1, 0, 1, 0,
        1, 0, 1, 0, 1,
        0, 1, 0, 1, 0,
        1,1,1,0,0,1,1,0
    ]
})
X=data['Text']
y=data['Label']
#split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
#vectorise
vectorizer=TfidfVectorizer()
X_vec=vectorizer.fit_transform(X_train)
vec_test=vectorizer.transform(X_test)
model=LogisticRegression()
model.fit(X_vec,y_train)
test_input=[input("Enter your review: ")]
#vectorize
inp_vectorise=vectorizer.transform(test_input)
prediction=model.predict(inp_vectorise)
print("Positive" if prediction[0]==1 else "Negative")