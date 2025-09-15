import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import re

try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

try:
    nltk.data.find('vader_lexicon')
except LookupError:
    nltk.download('vader_lexicon')


class TextAnalyzer:
    def __init__(self):
        self.sia = SentimentIntensityAnalyzer()
        self.stemmer = PorterStemmer()
        self.stop_words = set(stopwords.words('english'))
    
    def analyze_sentiment(self, text):
        if not text or not isinstance(text, str):
            return {"error": "Invalid input text"}
        
        scores = self.sia.polarity_scores(text)
        
        if scores['compound'] >= 0.05:
            sentiment = 'positive'
        elif scores['compound'] <= -0.05:
            sentiment = 'negative'
        else:
            sentiment = 'neutral'
        
        return {
            'sentiment': sentiment,
            'scores': scores
        }
    
    def summarize_text(self, text, num_sentences=3):
        if not text or not isinstance(text, str):
            return {"error": "Invalid input text"}
        
        sentences = sent_tokenize(text)
        
        if len(sentences) <= num_sentences:
            return ' '.join(sentences)
        
        word_freq = {}
        words = word_tokenize(text.lower())
        
        for word in words:
            if word.isalnum() and word not in self.stop_words:
                stemmed_word = self.stemmer.stem(word)
                word_freq[stemmed_word] = word_freq.get(stemmed_word, 0) + 1
        
        sentence_scores = {}
        for sentence in sentences:
            words = word_tokenize(sentence.lower())
            score = 0
            word_count = 0
            
            for word in words:
                if word.isalnum() and word not in self.stop_words:
                    stemmed_word = self.stemmer.stem(word)
                    if stemmed_word in word_freq:
                        score += word_freq[stemmed_word]
                        word_count += 1
            
            if word_count > 0:
                sentence_scores[sentence] = score / word_count
        
        top_sentences = sorted(sentence_scores.items(), key=lambda x: x[1], reverse=True)[:num_sentences]
        summary_sentences = [sentence[0] for sentence in top_sentences]
        
        original_order = []
        for sentence in sentences:
            if sentence in summary_sentences:
                original_order.append(sentence)
        
        return ' '.join(original_order)
    
    def get_word_frequency(self, text):
        if not text or not isinstance(text, str):
            return {"error": "Invalid input text"}
        
        words = word_tokenize(text.lower())
        word_freq = {}
        
        for word in words:
            if word.isalnum() and word not in self.stop_words:
                stemmed_word = self.stemmer.stem(word)
                word_freq[stemmed_word] = word_freq.get(stemmed_word, 0) + 1
        
        return dict(sorted(word_freq.items(), key=lambda x: x[1], reverse=True))