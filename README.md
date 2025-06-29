CYBER ABUSE RECOGNITION SYSTEM USING BERT

-->About the Project

Cyberbullying is a serious threat in today's digital age, especially on social media platforms. 
This project presents a Machine Learning-powered web application that detects abusive or harmful online messages in real time.

Designed with Flask and trained on a real-world dataset, the app offers user-friendly interaction, authentication, and precise predictions.


-->Objectives

- Detect and classify cyber abuse with high accuracy.
- Provide an intuitive, secure, and responsive web interface.
- Empower moderation teams and platforms with early detection tools.


-->Technologies Used

| Area             | Tools/Technologies                     |
|------------------|----------------------------------------|
| Programming      | Python                                 |
| Web Framework    | Flask                                  |
| ML Model         | Logistic Regression                    |
| Data Processing  | Pandas, NLTK                           |
| Vectorization    | TF-IDF                                 |
| Frontend         | HTML, Bootstrap                        |
| Authentication   | SQLite Database                        |
| Deployment Ready | Render / Heroku Compatible             |


-->Dataset Details

- Source: Public JSON Cyberbullying Dataset (Google Drive)
- Size: ~25,000 labeled texts
- Labels: `1 = Cyberbullying`, `0 = Safe`
- Preprocessing: Stopword removal, punctuation removal, lowercasing


-->Model Performance

- Algorithm: Logistic Regression
- Accuracy: ~90%
- Vectorizer: TF-IDF (max_features = 5000)
- Evaluation: Train-Test Split (80-20)


-->Features

-User Registration & Login (SQLite)
-Text Input Interface
-Abuse Prediction (Real-time)
-Trained ML Model (TF-IDF + Logistic Regression)
-Result Display (Safe or Cyberbullying)

--> How to Run Locally

```bash
# Step 1: Clone the repo
git clone https://github.com/yourusername/cyber-abuse-detection.git
cd cyber-abuse-detection

# Step 2: Install dependencies
pip install -r requirements.txt

# Step 3: Run the app
python apps.py

--> screenshots

### 🔐 Login Page  
<img src="screenshots/login.png" width="500"/>

### 🏠 Home Page  
<img src="screenshots/home.png" width="500"/>

### ⚠️ Prediction Result  
<img src="screenshots/result.png" width="500"/>

