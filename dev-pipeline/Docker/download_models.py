"""
Script to download required models during Docker build.
This pre-downloads models so they're available in the container.
"""
import os
import torch
# import spacy
from transformers import AutoTokenizer, AutoModelForSequenceClassification, AutoConfig
# import nltk

def main():
    print("Starting model downloads...")
    
    # Create models directory
    os.makedirs("/app/models", exist_ok=True)
    
    # 1. Download sentiment analysis model
    print("Downloading sentiment analysis model...")
    MODEL = "cardiffnlp/twitter-roberta-base-sentiment-latest"
    tokenizer = AutoTokenizer.from_pretrained(MODEL)
    config = AutoConfig.from_pretrained(MODEL)
    model_sentiment = AutoModelForSequenceClassification.from_pretrained(MODEL)
    
    # Save models to disk to avoid re-downloading
    tokenizer.save_pretrained("/app/models/sentiment_tokenizer")
    config.save_pretrained("/app/models/sentiment_config")
    model_sentiment.save_pretrained("/app/models/sentiment_model")
    print("Sentiment analysis model downloaded successfully.")

    # # 2. Download SpaCy models
    # print("Downloading SpaCy models...")
    # spacy.cli.download("en_core_web_sm")
    # spacy.cli.download("en_core_web_md")
    # print("SpaCy models downloaded successfully.")
    
    # # 3. Download NLTK data
    # print("Downloading NLTK data...")
    # nltk.download('punkt')
    # nltk.download('stopwords')
    # nltk.download('wordnet')
    # print("NLTK data downloaded successfully.")
    
    print("All models downloaded successfully!")

if __name__ == "__main__":
    main()