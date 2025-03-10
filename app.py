import streamlit as st
from transformers import pipeline

# Load the sentiment analysis pipeline
sentiment_pipeline = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")

def get_sentiment_label(text):
    result = sentiment_pipeline(text)[0]
    score = result['label'][0]  # Extract first character (rating 1-5)
    score = int(score) if score.isdigit() else 3  # Default to neutral if not a digit
    
    if score >= 4:
        return "Positive 😊"
    elif score == 3:
        return "Neutral 😐"
    else:
        return "Negative 😞"

# Streamlit UI
st.title("Sentiment Analysis App")
user_input = st.text_area("Enter your text:", "")

if st.button("Analyze"):
    if user_input.strip():
        sentiment = get_sentiment_label(user_input)
        st.write(f"**Sentiment:** {sentiment}")
    else:
        st.warning("Please enter some text for analysis!")
