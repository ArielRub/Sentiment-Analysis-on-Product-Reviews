from sklearn.feature_extraction.text import CountVectorizer

def extract_features(preprocessed_reviews, sentiments):
    print("Extracting features using Bag of Words model...")
    # Creating the Bag of Words model
    cv = CountVectorizer(max_features = 1500)
    
    # X contains the features, y contains the labels
    X = cv.fit_transform(preprocessed_reviews).toarray()
    
    # Assuming that you have sentiment labels in your data
    # Placeholder here - you need to replace this part with your actual labels
    y = sentiments
    print("Features extracted.\n")
    print(f"Number of samples in X: {len(X)}")
    print(f"Number of samples in y: {len(y)}")
    return X, y
