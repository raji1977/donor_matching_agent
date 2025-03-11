from flask import Flask, request, jsonify
import sqlite3
import numpy as np
import pickle
from sklearn.neighbors import KNeighborsClassifier

app = Flask(__name__)

# Database setup
def create_database():
    conn = sqlite3.connect("donors.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS donors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            blood_group TEXT,
            location TEXT,
            last_donation INTEGER
        )
    """)
    conn.commit()
    conn.close()

# Sample donor data
def insert_sample_data():
    conn = sqlite3.connect("donors.db")
    cursor = conn.cursor()
    sample_donors = [
        ("Alice", "O+", "New York", 30),
        ("Bob", "A+", "Los Angeles", 60),
        ("Charlie", "B+", "Chicago", 15),
        ("David", "O-", "Houston", 90)
    ]
    cursor.executemany("INSERT INTO donors (name, blood_group, location, last_donation) VALUES (?, ?, ?, ?)", sample_donors)
    conn.commit()
    conn.close()

# Train AI model
def train_ai_model():
    conn = sqlite3.connect("donors.db")
    cursor = conn.cursor()
    cursor.execute("SELECT blood_group, location, last_donation FROM donors")
    data = cursor.fetchall()
    conn.close()
    
    if not data:
        return None
    
    X = np.array([[hash(bg) % 100, hash(loc) % 100, ld] for bg, loc, ld in data])
    y = np.arange(len(data))  # Dummy labels for training
    
    model = KNeighborsClassifier(n_neighbors=1)
    model.fit(X, y)
    
    with open("donor_model.pkl", "wb") as f:
        pickle.dump(model, f)

# Load AI model
def load_ai_model():
    with open("donor_model.pkl", "rb") as f:
        return pickle.load(f)

# AI-powered donor matching
@app.route("/match-donor", methods=["POST"])
def match_donor():
    data = request.json
    blood_group = data.get("blood_group")
    location = data.get("location")
    
    if not blood_group or not location:
        return jsonify({"error": "Blood group and location are required"}), 400
    
    conn = sqlite3.connect("donors.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name, blood_group, location, last_donation FROM donors")
    donors = cursor.fetchall()
    conn.close()
    
    if not donors:
        return jsonify({"message": "No donors available"}), 404
    
    model = load_ai_model()
    X_query = np.array([[hash(blood_group) % 100, hash(location) % 100, 0]])
    match_index = model.predict(X_query)[0]
    matched_donor = donors[match_index]
    
    return jsonify({"best_match": {"name": matched_donor[0], "blood_group": matched_donor[1], "location": matched_donor[2]}})

if __name__ == "__main__":
    create_database()
    insert_sample_data()
    train_ai_model()
    app.run(debug=True)
