from setuptools import setup, find_packages

setup(
    name="textanalyzer",
    version="0.1.0",
    description="A Python library for text processing and analysis",
    packages=find_packages(),
    install_requires=[
        "requests",
        "beautifulsoup4",
        "nltk",
    ],
    python_requires=">=3.7",
    author="Sivan",
    author_email="Sivan.gruner@gmail.com",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
