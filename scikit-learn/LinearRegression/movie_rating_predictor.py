import tkinter as tk
from tkinter import ttk, messagebox
from sklearn.linear_model import LinearRegression
import pandas as pd
#THIS IS FROM CHATGPT
# 🔹 Sample Data
data = pd.DataFrame({
    'Watch_Time_Minutes': [30, 60, 45, 90, 120, 80, 70, 150, 100, 110],
    'Genre_Code':         [1, 2, 1, 3, 2, 3, 1, 2, 3, 2],  # 1 = Comedy, 2 = Action, 3 = Drama
    'Friends_Watched':    [2, 5, 1, 6, 10, 3, 2, 9, 4, 8],
    'Rating':             [5.0, 7.5, 4.5, 8.0, 9.0, 6.5, 5.0, 9.5, 7.0, 8.5]
})

# 🔹 Train the Model
model = LinearRegression()
model.fit(data[['Watch_Time_Minutes', 'Genre_Code', 'Friends_Watched']], data['Rating'])

# 🔹 Genre Mapping
genre_map = {
    "Comedy": 1,
    "Action": 2,
    "Drama": 3
}

# 🔹 Predict Function
def predict_rating():
    try:
        watch = int(entry_watch.get())
        friends = int(entry_friends.get())
        genre_name = genre_combo.get()

        if genre_name not in genre_map:
            messagebox.showerror("Error", "Please select a valid genre.")
            return

        genre = genre_map[genre_name]

        # Prediction
        input_df = pd.DataFrame({
            'Watch_Time_Minutes': [watch],
            'Genre_Code': [genre],
            'Friends_Watched': [friends]
        })
        prediction = model.predict(input_df)[0]
        final_rating = max(0, min(prediction, 10))  # Cap 0–10

        result_label.config(text=f"🎯 Predicted Rating: {final_rating:.2f}")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric inputs.")

# 🔹 Setup GUI Window
root = tk.Tk()
root.title("🎬 Movie Rating Predictor")
root.geometry("400x400")
root.configure(bg="#f8f8f8")

# 🔹 Title
tk.Label(root, text="AI Movie Rating Predictor", font=("Helvetica", 16, "bold"), bg="#f8f8f8", fg="#333").pack(pady=20)

# 🔹 Main Frame
frame = tk.Frame(root, bg="#f8f8f8")
frame.pack(pady=10)

# Watch Time Input
tk.Label(frame, text="Watch Time (minutes):", font=("Arial", 12), bg="#f8f8f8").grid(row=0, column=0, sticky='w', padx=10, pady=5)
entry_watch = tk.Entry(frame, font=("Arial", 12), width=20)
entry_watch.grid(row=0, column=1, pady=5)

# Genre Dropdown
tk.Label(frame, text="Genre:", font=("Arial", 12), bg="#f8f8f8").grid(row=1, column=0, sticky='w', padx=10, pady=5)
genre_combo = ttk.Combobox(frame, values=list(genre_map.keys()), font=("Arial", 12), state="readonly")
genre_combo.grid(row=1, column=1, pady=5)
genre_combo.set("Select Genre")

# Friends Watched
tk.Label(frame, text="Friends Watched:", font=("Arial", 12), bg="#f8f8f8").grid(row=2, column=0, sticky='w', padx=10, pady=5)
entry_friends = tk.Entry(frame, font=("Arial", 12), width=20)
entry_friends.grid(row=2, column=1, pady=5)

# Predict Button
tk.Button(root, text="Predict Rating", command=predict_rating,
          font=("Arial", 12, "bold"), bg="#007acc", fg="white", width=20).pack(pady=20)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), bg="#f8f8f8", fg="#222")
result_label.pack(pady=10)

# 🔹 Start GUI
root.mainloop()
