# 📊 WhatsApp Chat Analyzer

A **Streamlit-based data analysis and machine learning application** that analyzes WhatsApp chat data to uncover insights about user behavior, messaging patterns, emoji usage, and activity trends.

---

## 🚀 Features

### 📈 Chat Analysis
- Total messages, words, links, and media count  
- Monthly and daily message timeline  
- Most active users  
- Activity heatmap (day vs hour)

### 😀 Emoji & Media Analysis
- Most used emojis  
- Emoji distribution (table + pie chart)  
- Media and link sharing behavior  

### 🤖 Machine Learning (No NLP)
- Night vs Day message prediction (Classification)  
- Feature engineering on temporal & behavioral data  
- Random Forest model with ~82% accuracy  
- Confusion matrix & feature importance  

> ⚠️ NLP is intentionally avoided. Machine learning is applied only on structured data.

---

## 🧠 Machine Learning Details

**Features Used**
- Day of month  
- Weekday  
- Weekend indicator  
- Month number  
- Log-normalized message length  

**Model**
- Random Forest Classifier  
- Proper train-test split  
- Data leakage handled  
- Realistic evaluation  

---

## 🛠️ Tech Stack

- Python  
- Streamlit  
- Pandas, NumPy  
- Matplotlib, Seaborn  
- Scikit-learn  
- Emoji, URLExtract  

---

## 📂 Project Structure

whatsapp-chat-analyzer/

│
├── app.py # Streamlit app

├── helper.py # Analysis & ML helpers

├── preprocessor.py # WhatsApp chat parser

├── requirements.txt # Dependencies

├── Procfile # Render deployment

├── .streamlit/

│ └── config.toml

└── README.md

☁️ Deployment

The application is deployed on Render using Streamlit.

streamlit run app.py --server.port=$PORT --server.address=0.0.0.0

🎯 Learning Outcomes

End-to-end data analysis project

Feature engineering on real-world data

Applied machine learning without NLP

Model evaluation and interpretation

Cloud deployment using Render

👩‍💻 Author

Dipshikha
BS in Data Science – IIT Madras
Aspiring Data Scientist & ML Engineer
