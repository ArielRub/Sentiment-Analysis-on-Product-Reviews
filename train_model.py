import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import classification_report
print("Splitting dataset into training and test sets...")
def split_data(X, y, test_size=0.2, random_state=42):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
    print("Unique classes in y_train:", np.unique(y_train))
    return X_train, X_test, y_train, y_test


def train_model(X_train, y_train):
    # Create SVM model
    clf = svm.SVC(kernel='linear')

    # Train the model
    clf.fit(X_train, y_train)

    return clf

def evaluate_model(model, X_test, y_test):
    # Make predictions on the test set
    y_pred = model.predict(X_test)

    # Print the classification report
    print(classification_report(y_test, y_pred))
