#!/usr/bin/env python3
"""
Test script to verify TextAnalyzer package functionality.
"""

from TextAnalyzer import TextAnalyzer
from TextAnalyzer.utils.text_ops import clean_text, extract_urls
from TextAnalyzer.config.settings import Config


def test_text_cleaning():
    """Test text cleaning functionality."""
    print("=== Testing Text Cleaning ===")
    test_text = "  Hello    World!  This   is  a   test.  "
    cleaned = clean_text(test_text)
    print(f"Original: '{test_text}'")
    print(f"Cleaned:  '{cleaned}'")
    print()


def test_url_extraction():
    """Test URL extraction functionality."""
    print("=== Testing URL Extraction ===")
    test_text = "Visit https://example.com and http://google.com for more info"
    urls = extract_urls(test_text)
    print(f"Text: {test_text}")
    print(f"URLs found: {urls}")
    print()


def test_sentiment_analysis():
    """Test sentiment analysis functionality."""
    print("=== Testing Sentiment Analysis ===")
    analyzer = TextAnalyzer()

    test_texts = [
        "This library is amazing and wonderful!",
        "I hate this terrible software.",
        "The weather is okay today.",
        "Python is a programming language.",
    ]

    for text in test_texts:
        result = analyzer.analyze_sentiment(text)
        print(f"Text: '{text}'")
        print(f"Sentiment: {result['sentiment']}")
        print(f"Scores: {result['scores']}")
        print()


def test_text_summarization():
    """Test text summarization functionality."""
    print("=== Testing Text Summarization ===")
    analyzer = TextAnalyzer()

    long_text = """
    Natural language processing (NLP) is a subfield of linguistics, computer science, 
    and artificial intelligence concerned with the interactions between computers and human language.
    In particular, how to program computers to process and analyze large amounts of natural language data.
    The goal is a computer capable of understanding the contents of documents, including the contextual 
    nuances of the language within them. The technology can then accurately extract information and 
    insights contained in the documents as well as categorize and organize the documents themselves.
    NLP combines computational linguistics with statistical, machine learning, and deep learning models.
    These technologies enable computers to process human language in the form of text or voice data 
    and to understand its full meaning, complete with the speaker or writer's intent and sentiment.
    """

    summary = analyzer.summarize_text(long_text, num_sentences=2)
    print(f"Original text length: {len(long_text)} characters")
    print(f"Summary: {summary}")
    print(f"Summary length: {len(summary)} characters")
    print()


def test_word_frequency():
    """Test word frequency analysis."""
    print("=== Testing Word Frequency Analysis ===")
    analyzer = TextAnalyzer()

    text = "Python is great. Python is powerful. Programming with Python is fun and Python makes coding easy."
    freq = analyzer.get_word_frequency(text)

    print(f"Text: {text}")
    print("Top word frequencies:")
    for word, count in list(freq.items())[:5]:
        print(f"  {word}: {count}")
    print()


def test_config():
    """Test configuration settings."""
    print("=== Testing Configuration ===")
    print(f"Request timeout: {Config.REQUEST_TIMEOUT}")
    print(f"User agent: {Config.USER_AGENT}")
    print(f"Debug mode: {Config.DEBUG}")
    print()


def main():
    """Run all tests."""
    # Import and print package version
    try:
        from TextAnalyzer import __version__

        print(f"Testing TextAnalyzer Package v{__version__}\n")
    except ImportError:
        print("Testing TextAnalyzer Package\n")

    try:
        test_config()
        test_text_cleaning()
        test_url_extraction()
        test_sentiment_analysis()
        test_word_frequency()
        test_text_summarization()

        print("✅ All tests completed successfully!")

    except Exception as e:
        print(f"❌ Error during testing: {e}")
        import traceback

        traceback.print_exc()


if __name__ == "__main__":
    main()
