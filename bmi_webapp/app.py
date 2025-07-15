from flask import Flask, render_template, request, redirect, url_for, session, send_file
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
import matplotlib.pyplot as plt
from io import BytesIO
from datetime import datetime

# Correct Flask initialization
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a strong random string in production

# Create tables if they don’t exist
def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT,
    gender TEXT
)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS bmi_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        weight REAL,
        height REAL,
        bmi REAL,
        category TEXT,
        timestamp TEXT
    )''')
    conn.commit()
    conn.close()

init_db()  # Ensure tables are created

# BMI Category Function
def categorize_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

# Routes
@app.route('/')
def home():
    return redirect('/login')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = generate_password_hash(request.form['password'])
        gender = request.form['gender']  # Get gender from form
        try:
            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (username, password, gender) VALUES (?, ?, ?)", (username, password, gender))  # Save gender
            conn.commit()
            conn.close()
            return redirect('/login')
        except:
            return "Username already exists!"
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password_input = request.form['password']
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        user = cursor.fetchone()
        conn.close()
        if user and check_password_hash(user[2], password_input):
            session['user_id'] = user[0]
            session['username'] = user[1]
            session['gender'] = user[3]  

            return redirect('/dashboard')
        else:
            return "Invalid credentials"
    return render_template('login.html')

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if 'user_id' not in session:
        return redirect('/login')

    if request.method == 'POST':
        weight = float(request.form['weight'])
        height = float(request.form['height'])
        bmi = round(weight / (height ** 2), 2)
        category = categorize_bmi(bmi)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO bmi_data (user_id, weight, height, bmi, category, timestamp) VALUES (?, ?, ?, ?, ?, ?)",
                       (session['user_id'], weight, height, bmi, category, timestamp))
        conn.commit()
        conn.close()

        return render_template('bmi_result.html', bmi=bmi, category=category)

    return render_template('dashboard.html', username=session['username'])

@app.route('/history')
def history():
    if 'user_id' not in session:
        return redirect('/login')

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT timestamp, bmi FROM bmi_data WHERE user_id = ?", (session['user_id'],))
    data = cursor.fetchall()
    conn.close()

    if not data:
        return "No BMI records found."

    timestamps, bmis = zip(*data)

    plt.figure(figsize=(10, 4))
    plt.plot(timestamps, bmis, marker='o', linestyle='--', color='blue')
    plt.xticks(rotation=45)
    plt.xlabel("Timestamp")
    plt.ylabel("BMI")
    plt.title(f"{session['username']}'s BMI Trend")
    plt.tight_layout()

    buf = BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    return send_file(buf, mimetype='image/png')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')

#Run the app
if __name__ == '__main__':
    app.run(debug=True)
