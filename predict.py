import joblib

model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")
new_text = ["Invoice Number INV1001 Amount 500 Euro"]

new_vector = vectorizer.transform(new_text)

result = model.predict(new_vector)

print(result[0])