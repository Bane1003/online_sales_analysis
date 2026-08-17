import pandas as pd

# Load the file
df = pd.read_csv("data/reviews_with_predicted_sentiment_openai.csv")

# Check if the required columns exist
required_columns = ["sentiment", "predicted_sentiment"]

for column in required_columns:
    if column not in df.columns:
        raise ValueError(f"Missing column: {column}")

# Normalize values
real_sentiment = df["sentiment"].astype(str).str.strip().str.lower()
predicted_sentiment = df["predicted_sentiment"].astype(str).str.strip().str.lower()

# Compare real and predicted values
correct_predictions = real_sentiment == predicted_sentiment

# Count correct predictions
correct_count = correct_predictions.sum()

# Count total rows
total_count = len(df)

# Calculate accuracy percentage
accuracy = correct_count / total_count * 100

# Display results
print(f"Correct predictions: {correct_count}/{total_count}")
print(f"Accuracy: {accuracy:.2f}%")