# AI-Powered Blood Donor Matching System

## 📌 Project Overview
This project is an AI-driven Blood Donor Matching System that connects blood donors with recipients based on **blood group** and **location**. It utilizes a **Flask backend, SQLite database, and a K-Nearest Neighbors (KNN) AI model** to find the best donor match.

## 🚀 Features
- 🩸 **AI-Based Donor Matching**: Uses KNN to recommend the most suitable donor.
- 🔎 **Search by Blood Group & Location**: Ensures accurate matches.
- 🗂️ **Database Integration**: Stores donor details in SQLite.
- 🌐 **Simple UI**: Built with HTML, CSS, and JavaScript.

## 🏗️ Tech Stack
- **Backend**: Python (Flask)
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite
- **AI Model**: K-Nearest Neighbors (KNN) using `scikit-learn`

## 🛠️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone <your-repo-link>
cd blood-donor-matching
```

### 2️⃣ Install Dependencies
```bash
pip install flask numpy scikit-learn
```

### 3️⃣ Run the Flask Server
```bash
python script.py
```
You should see:
```
Running on http://127.0.0.1:5000/
```

### 4️⃣ Open the Frontend
1. Open `index.html` in a browser.
2. Enter **blood group & location**.
3. Click **Find Donor**.
4. The AI model will recommend the best donor match!

## 📬 API Endpoint
### `POST /match-donor`
#### Request Body (JSON):
```json
{
  "blood_group": "B+",
  "location": "Vijayawada"
}
```
#### Response Example:
```json
{
  "best_match": {
    "name": "Alice",
    "blood_group": "O+",
    "location": "New York"
  }
}
```

## 📝 License
This project is for educational purposes. Feel free to modify and improve it.

## ✨ Author
Developed for a hackathon. Best of luck! 🚀

