from flask import Flask, render_template, request, redirect, session
import pickle
import os
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Load ML Model
vectorizer = pickle.load(open('model/tfidf_vectorizer.pkl', 'rb'))
model = pickle.load(open('model/logistic_model.pkl', 'rb'))

# SQLite Setup
def init_db():
    with sqlite3.connect("users.db") as conn:
        conn.execute('CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)')
init_db()

@app.route('/')
def index():
    if 'username' in session:
        return render_template('index.html', username=session['username'])
    return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        uname = request.form['username']
        pwd = request.form['password']
        with sqlite3.connect("users.db") as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (uname, pwd))
            if cursor.fetchone():
                session['username'] = uname
                return redirect('/')
            else:
                return "Invalid login"
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        uname = request.form['username']
        pwd = request.form['password']
        with sqlite3.connect("users.db") as conn:
            conn.execute("INSERT INTO users (username, password) VALUES (?, ?)", (uname, pwd))
        return redirect('/login')
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/login')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        message = request.form['message']
        data = vectorizer.transform([message])
        prediction = model.predict(data)
        result = "Cyberbullying Detected" if prediction[0] == 1 else "No Cyberbullying"
        return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
