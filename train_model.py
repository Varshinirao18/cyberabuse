import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import pickle
import nltk
import re
import string

# Download stopwords
nltk.download('stopwords')
from nltk.corpus import stopwords
stop_words = stopwords.words('english')

# Step 1: Load dataset
url = 'https://drive.google.com/uc?export=download&id=12fBlhsa5GIdtme1jT3KlPPIgIdjzqhv1'
df = pd.read_json(url, lines=True)

# Step 2: Preprocess the dataset
def clean_text(text):
    text = text.lower()
    text = re.sub(f'[{re.escape(string.punctuation)}]', '', text)  # Remove punctuation
    text = ' '.join(word for word in text.split() if word not in stop_words)  # Remove stopwords
    return text

df['clean_text'] = df['content'].apply(clean_text)
df['label'] = df['annotation'].apply(lambda x: 1 if x['label'][0] == '1' else 0)

# Step 3: Features and labels
X = df['clean_text']
y = df['label']

# Step 4: Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 5: Vectorize the text
vectorizer = TfidfVectorizer(max_features=5000)
X_train_vec = vectorizer.fit_transform(X_train)

# Step 6: Train the model
model = LogisticRegression()
model.fit(X_train_vec, y_train)

# Step 7: Save the model and vectorizer
import os
os.makedirs('model', exist_ok=True)

pickle.dump(vectorizer, open('model/tfidf_vectorizer.pkl', 'wb'))
pickle.dump(model, open('model/logistic_model.pkl', 'wb'))

print("✅ Model and Vectorizer saved successfully in the /model folder!")
