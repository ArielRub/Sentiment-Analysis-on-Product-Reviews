import pandas as pd
from preprocess_reviews import preprocess_reviews
from feature_extraction import extract_features
from train_model import split_data, train_model, evaluate_model

def main():
    # Step 1: Load reviews from CSV
    print("Loading reviews from CSV...")
    filepath = "amazon.csv"
    df = pd.read_csv(filepath)

    # Print DataFrame columns
    print(df.columns)

    # Strip leading/trailing white spaces from column names
    df.columns = df.columns.str.strip()

    reviews = df['reviewText'].tolist()
    sentiments = df['overall'].tolist()

    # Step 2: Preprocess reviews
    print("Preprocessing reviews...")
    preprocessed_reviews = preprocess_reviews(reviews)

    # Step 3: Feature extraction
    print("Extracting features using Bag of Words model...")
    X, y = extract_features(preprocessed_reviews, sentiments)

    # Step 4: Split data into training and testing sets
    print("Splitting dataset into training and test sets...")
    X_train, X_test, y_train, y_test = split_data(X, y)

    # Step 5: Train the model
    print("Training the model...")
    model = train_model(X_train, y_train)

    # Step 6: Evaluate the model
    print("Evaluating the model...")
    evaluate_model(model, X_test, y_test)

if __name__ == "__main__":
    main()
