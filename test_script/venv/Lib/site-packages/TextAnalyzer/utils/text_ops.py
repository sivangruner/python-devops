import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from ..config.settings import get_request_timeout, get_user_agent


def clean_text(text):
    if not text or not isinstance(text, str):
        return ""
    
    text = re.sub(r'\s+', ' ', text)
    text = text.strip()
    
    return text


def extract_urls(text):
    if not text or not isinstance(text, str):
        return []
    
    url_pattern = r'https?://(?:[-\w.])+(?:[:\d]+)?(?:/(?:[\w/_.])*(?:\?(?:[\w&=%.])*)?(?:#(?:[\w.])*)?)?'
    urls = re.findall(url_pattern, text)
    
    return urls


def fetch_web_content(url, timeout=None):
    if not url or not isinstance(url, str):
        return {"error": "Invalid URL"}
    
    try:
        parsed_url = urlparse(url)
        if not all([parsed_url.scheme, parsed_url.netloc]):
            return {"error": "Invalid URL format"}
        
        timeout = timeout or get_request_timeout()
        headers = {'User-Agent': get_user_agent()}
        
        response = requests.get(url, headers=headers, timeout=timeout)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        for script in soup(["script", "style"]):
            script.decompose()
        
        text = soup.get_text()
        text = clean_text(text)
        
        return {
            "url": url,
            "title": soup.title.string if soup.title else "",
            "content": text,
            "status_code": response.status_code
        }
        
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}
    except Exception as e:
        return {"error": f"Error processing content: {str(e)}"}


def remove_stopwords(text, custom_stopwords=None):
    if not text or not isinstance(text, str):
        return ""
    
    try:
        from nltk.corpus import stopwords
        from nltk.tokenize import word_tokenize
        
        stop_words = set(stopwords.words('english'))
        if custom_stopwords:
            stop_words.update(custom_stopwords)
        
        words = word_tokenize(text.lower())
        filtered_text = ' '.join([word for word in words if word.lower() not in stop_words and word.isalnum()])
        
        return filtered_text
        
    except ImportError:
        return text


def extract_sentences(text):
    if not text or not isinstance(text, str):
        return []
    
    try:
        from nltk.tokenize import sent_tokenize
        return sent_tokenize(text)
    except ImportError:
        sentence_endings = r'[.!?]+\s+'
        sentences = re.split(sentence_endings, text)
        return [s.strip() for s in sentences if s.strip()]