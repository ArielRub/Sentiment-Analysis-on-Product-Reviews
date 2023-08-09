Sentiment Analysis on Product Reviews
Project Description
This project involves performing sentiment analysis on a collection of product reviews. The purpose is to classify the sentiment of the review into one of the five categories (1 to 5), where '1' indicates a negative sentiment and '5' indicates a positive sentiment. The project uses the Natural Language Toolkit (NLTK) for text preprocessing and scikit-learn for model training and evaluation.

Requirements
Python 3.6 or higher
pandas
numpy
scikit-learn
NLTK (with the stopwords package)
Installation
Ensure that you have Python installed on your machine. You can verify this by running the following command in the terminal:
'python --version'

Install the necessary Python packages using pip:
pip install pandas numpy scikit-learn nltk

Download the NLTK stopwords package using the Python interpreter:
import nltk
nltk.download('stopwords')

Running the Code
Place your CSV file containing product reviews in the same directory as the script files.

In 'main.py', make sure the filename variable points to your CSV file:
 filename = 'your_file_name.csv'

Run 'main.py' from the terminal:
    python main.py

The program will read the data, preprocess the reviews, extract features using a Bag of Words model, split the data into training and test sets, and then train and evaluate a multinomial Naive Bayes model. The evaluation results will be printed to the console.

Note
The current implementation expects the review text to be in a column named 'reviewText'. If your data uses a different column name, please adjust the code accordingly.

