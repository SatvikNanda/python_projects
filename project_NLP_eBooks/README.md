# Natural language processing of e-book

## Overview:
The NLP eBook Analysis Project is a Python-based application that performs natural language processing on eBooks to analyze various linguistic features. The project leverages libraries like NLTK to extract insights from the text. The analysis includes tasks like word frequency distribution, sentiment analysis and more.

## Features:
Word Frequency Analysis: Identify and visualize the most common words in the eBook.<br>
Sentiment Analysis: Determine the overall sentiment of the text.<br>
Named Entity Recognition: Extract and classify named entities (e.g., people, locations) from the text.<br>
Sentence Search with Regular Expressions: Find and extract sentences containing a specific word.<br>

## Methodology:
### Data Preparation:
Loading the eBook: The text of the eBook is loaded into the application for analysis.<br>
Counting Chapters: Regular expressions (regex) are used to identify and count the number of chapters in the eBook.<br>

### Sentence Search with Regular Expressions:
Finding Specific Words: Regular expressions are employed to find all sentences that contain a specific word. This helps in understanding the context and frequency of important terms within the text.<br>

### Word Frequency Analysis:
Most Used Words: Regular expressions are used to calculate the frequency of each word in the text.<br>
Non-Article Words: The NLTK library is used to filter out common articles and identify the most frequently used non-article words.<br>

### Sentiment Analysis:
Chapter Sentiment: Sentiment analysis is performed to determine whether each chapter has a positive or negative sentiment. This involves calculating sentiment scores for each chapter to gauge the overall emotional tone.<br>

