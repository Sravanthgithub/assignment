#Develop an API server on python using Fast API for the model created in the previous step.

from string import punctuation 
from nltk.tokenize import word_tokenize
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from os.path import dirname, join, realpath
import joblib
import uvicorn
from fastapi import FastAPI
import requests as r
from pyramid.config import Configurator
import transformers
#from pyramid_swagger import add_swagger_view

app = FastAPI(
    title="Sentiment Analysis API",
    description="A simple API that use NLP model to predict the sentiment of the airline reviews",
    version="0.1",
)

# Load the model
model = joblib.load('Models/sentiment_classifier.pkl')
vectorizer = joblib.load('Models/vectorizer.pkl')

class Inference:
    def __init__(self, model, vectorizer):
        self.model = model
        self.vectorizer = vectorizer

    def get_sentiment(self, review):
        new_review = [review]
        new_review = self.vectorizer.transform(new_review)
        pred = self.model.predict(new_review)
        if pred == 1:
            return 'Positive'
        else:
            return 'Negative'

inference = Inference(model, vectorizer)

@app.get("/")
def home():
    return {"message": "Welcome to Sentiment Analysis API"}

@app.get("/predict/{review}")
def predict_sentiment(review: str):
    return {"sentiment": inference.get_sentiment(review)}







