import nltk
nltk.download('stopwords')


import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

def preprocess_reviews(reviews):
    processed_reviews = []
    stemmer = PorterStemmer()
    for review in reviews:
        # Convert review to string
        review = str(review)

        # Remove all the special characters
        review = re.sub(r'\W', ' ', review)

        # Remove all single characters
        review = re.sub(r'\s+[a-zA-Z]\s+', ' ', review)

        # Remove single characters from the start
        review = re.sub(r'\^[a-zA-Z]\s+', ' ', review) 

        # Substituting multiple spaces with single space
        review = re.sub(r'\s+', ' ', review, flags=re.I)

        # Removing prefixed 'b'
        review = re.sub(r'^b\s+', '', review)

        # Converting to lowercase
        review = review.lower()

        # Lemmatization
        review = review.split()
        review = [stemmer.stem(word) for word in review]
        review = ' '.join(review)
        
        processed_reviews.append(review)

    return processed_reviews
