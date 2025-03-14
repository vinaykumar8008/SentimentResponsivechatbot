# SentimentResponsivechatbot
Sentiment Analysis Chatbot 🤖📊

This is a Sentiment Analysis Chatbot built using Python, Tkinter, and Machine Learning.It analyzes user input to determine whether the sentiment is Positive 😊, Negative 😠, or Neutral 😐.

🚀 Features

✅ Uses Machine Learning (Naïve Bayes Classifier) for sentiment prediction✅ Preprocesses input (removes stopwords, punctuation, and lowercases text)✅ Interactive GUI built with Tkinter✅ Predicts sentiment in real-time

📌 Installation

1️⃣ Clone the Repository

git clone https://github.com/your-username/sentiment-chatbot.git
cd sentiment-chatbot

2️⃣ Install Dependencies

Make sure you have Python 3.x installed. Then install required packages:

pip install -r requirements.txt

3️⃣ Download NLTK Resources

import nltk
nltk.download('stopwords')

4️⃣ Train and Save the Sentiment Model

If you haven't trained a model yet, follow the steps in train_model.py to generate:

sentiment_model.pkl (Trained Model)

vectorizer.pkl (Text Vectorizer)

Alternatively, use the pre-trained models provided in the repo.

5️⃣ Run the Chatbot

python chatbot.py

📚 How It Works

The user enters a text message in the chatbot.

The chatbot preprocesses the input:

Converts text to lowercase

Removes punctuation & stopwords

Converts text into vectorized format using CountVectorizer

The trained ML model (sentiment_model.pkl) predicts the sentiment.

The chatbot displays the sentiment in a popup message.

🛠 Technologies Used

Python (Backend)

NLTK (Natural Language Processing)

Scikit-learn (Machine Learning Model)

Tkinter (GUI for chatbot)

Pickle (Saving & Loading ML Model)

🖼️ Screenshot



📌 Future Improvements

🚀 Upgrade to Deep Learning-based model (LSTM, BERT)🚀 Improve UI with a chatbot-style interface🚀 Add real-time speech-to-text support

📜 License

This project is licensed under the MIT License.

🤝 Contributing

Feel free to fork this repository and submit a pull request if you have any improvements!

🔗 Connect with Me

📧 Email: your.email@example.com🔗 LinkedIn: Your Profile🐖 GitHub: Your GitHub


