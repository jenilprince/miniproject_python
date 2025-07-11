import tkinter as tk
from tkinter import messagebox
from sklearn.linear_model import LinearRegression
import pandas as pd
#THIS IS FROM CHATGPT
# 🔹 Sample Training Data
data = pd.DataFrame({
    'Watch_Time_Minutes': [30, 60, 45, 90, 120, 80, 70, 150, 100, 110],
    'Genre_Code':         [1, 2, 1, 3, 2, 3, 1, 2, 3, 2],  # 1 = Comedy, 2 = Action, 3 = Drama
    'Friends_Watched':    [2, 5, 1, 6, 10, 3, 2, 9, 4, 8],
    'Rating':             [5.0, 7.5, 4.5, 8.0, 9.0, 6.5, 5.0, 9.5, 7.0, 8.5]
})

# 🔹 Train the Model
model = LinearRegression()
model.fit(data[['Watch_Time_Minutes', 'Genre_Code', 'Friends_Watched']], data['Rating'])

# 🔹 GUI Function
def predict_rating():
    try:
        watch = int(entry_watch.get())
        genre = int(entry_genre.get())
        friends = int(entry_friends.get())

        if genre not in [1, 2, 3]:
            messagebox.showerror("Input Error", "Genre code must be 1 (Comedy), 2 (Action), or 3 (Drama).")
            return

        # Predict
        input_df = pd.DataFrame({
            'Watch_Time_Minutes': [watch],
            'Genre_Code': [genre],
            'Friends_Watched': [friends]
        })
        prediction = model.predict(input_df)[0]
        final_rating = max(0, min(prediction, 10))  # Cap between 0–10

        # Show result
        result_label.config(text=f"Predicted Rating: {final_rating:.2f}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")

# 🔹 Create Tkinter Window
root = tk.Tk()
root.title("Movie Rating Predictor")
root.geometry("350x300")
root.configure(bg="#f0f0f0")

# 🔹 UI Labels and Entry Boxes
tk.Label(root, text="Watch Time (minutes):", bg="#f0f0f0").pack(pady=5)
entry_watch = tk.Entry(root)
entry_watch.pack()

tk.Label(root, text="Genre Code (1=Comedy, 2=Action, 3=Drama):", bg="#f0f0f0").pack(pady=5)
entry_genre = tk.Entry(root)
entry_genre.pack()

tk.Label(root, text="Friends Watched:", bg="#f0f0f0").pack(pady=5)
entry_friends = tk.Entry(root)
entry_friends.pack()

tk.Button(root, text="Predict Rating", command=predict_rating, bg="blue", fg="white").pack(pady=15)

# 🔹 Result Label
result_label = tk.Label(root, text="", font=("Arial", 14), bg="#f0f0f0")
result_label.pack()

# 🔹 Start GUI Loop
root.mainloop()
