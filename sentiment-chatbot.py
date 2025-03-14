import nltk
import pickle
import string
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from tkinter import Tk, Label, Entry, Button, messagebox

# Download NLTK resources
nltk.download('stopwords')

# Load pre-trained sentiment model (Assume we have trained & saved it)
with open("sentiment_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

# Load the vectorizer
with open("vectorizer.pkl", "rb") as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

def preprocess_text(text):
    """Preprocess the input text: lowercase, remove punctuation, and stopwords"""
    text = text.lower().translate(str.maketrans("", "", string.punctuation))
    words = text.split()
    words = [word for word in words if word not in stopwords.words("english")]
    return " ".join(words)

def analyze_sentiment(text):
    """Predict sentiment using ML model"""
    processed_text = preprocess_text(text)
    text_vectorized = vectorizer.transform([processed_text])
    sentiment = model.predict(text_vectorized)[0]
    return "Positive 😊" if sentiment == 1 else "Negative 😠" if sentiment == -1 else "Neutral 😐"

class ChatbotApp:
    def __init__(self, master):
        self.master = master
        master.title("Sentiment Analysis Chatbot")

        self.label = Label(master, text="Enter text:")
        self.label.pack()

        self.entry = Entry(master, width=50)
        self.entry.pack()

        self.button = Button(master, text="Analyze", command=self.analyze_text)
        self.button.pack()

    def analyze_text(self):
        user_input = self.entry.get()
        sentiment = analyze_sentiment(user_input)
        messagebox.showinfo("Sentiment Analysis Result", f"Sentiment: {sentiment}")

if __name__ == "__main__":
    root = Tk()
    app = ChatbotApp(root)
    root.mainloop()
