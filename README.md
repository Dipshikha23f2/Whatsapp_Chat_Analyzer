📊 WhatsApp Chat Analyzer

A Streamlit-based data analysis and machine learning application that analyzes WhatsApp chat data to uncover insights about user activity, messaging patterns, emoji usage, and behavioral trends.

🚀 Features
📈 Chat Analysis

Total messages, words, links, and media count

Monthly & daily message timeline

Most active users

Activity heatmap (day vs hour)

😀 Emoji & Media Analysis

Most used emojis

Emoji distribution (table + pie chart)

Media & link sharing behavior

🤖 Machine Learning (No NLP)

Night vs Day message prediction (Classification)

Feature engineering on temporal & behavioral data

Random Forest model with ~82% accuracy

Confusion matrix & feature importance

⚠️ No NLP or text modeling used — ML is applied only on structured features.

🧠 Machine Learning Approach
Features Used

Day of month

Weekday

Weekend indicator

Month number

Message length (log-normalized)

Model

Random Forest Classifier

Proper train-test split

Data leakage handled

Realistic performance evaluation

🛠️ Tech Stack

Python

Streamlit

Pandas, NumPy

Matplotlib, Seaborn

Scikit-learn

Emoji, URLExtract

📂 Project Structure
whatsapp-chat-analyzer/
│
├── app.py                # Streamlit app
├── helper.py             # Analysis & ML helpers
├── preprocessor.py       # WhatsApp chat parsing
├── requirements.txt      # Dependencies
├── Procfile              # Render deployment
├── .streamlit/
│   └── config.toml
└── README.md

📥 How to Use
1️⃣ Export WhatsApp Chat

Open WhatsApp

Export chat without media

Save as .txt

2️⃣ Run Locally
pip install -r requirements.txt
streamlit run app.py

3️⃣ Upload Chat File

Use Streamlit file uploader

Explore insights interactively

☁️ Deployment

The app is deployed on Render using:

Custom start command for Streamlit

Cloud-ready configuration

Lightweight ML models

streamlit run app.py --server.port=$PORT --server.address=0.0.0.0

🎯 Learning Outcomes

End-to-end data analysis project

Feature engineering on real-world data

Applied machine learning without NLP

Model evaluation & interpretation

Cloud deployment using Render

📌 Future Enhancements

User clustering (unsupervised ML)

Sentiment trends (optional)

Advanced visual dashboards

Downloadable reports

🙌 Author

Dipshikha
BS Data Science – IIT Madras
Aspiring Data Scientist & ML Engineer
