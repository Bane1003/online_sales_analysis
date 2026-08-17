from sklearn.naive_bayes import MultinomialNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.metrics import classification_report
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
import pandas as pd

# Load dataset
df = pd.read_csv("data/reviews_labeled_cleaned.csv")
X = df["review"]
y = df["sentiment"]
 
# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
 
# TF-IDF vectorization
vectorizer = TfidfVectorizer(ngram_range=(1,2), min_df=2)
X_train_tridf = vectorizer.fit_transform(X_train)
X_test_tridf = vectorizer.transform(X_test)

# Initialize models
models = {
    "Logistic Regression": LogisticRegression(max_iter=1000),
    "Naive Bayes": MultinomialNB(),
    "Decision Tree": DecisionTreeClassifier(),
    "Support Vector Machine": LinearSVC()
}
 
# Train, predict, and evaluate
for name, model in models.items():
    model.fit(X_train_tridf, y_train)
    y_pred = model.predict(X_test_tridf)
    print(f"\n{name} - Classification Report:")
    print(classification_report(y_test, y_pred))