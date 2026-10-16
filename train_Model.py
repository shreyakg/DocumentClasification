#Load the data
import pandas as pd
df = pd.read_excel("C:\\Users\\shreya.gurikar\\Documents\\UiPath\\Data_classification_Demo\\Train_Data.xlsx")

#Convert text to numbers
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["Text"])

#train model
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

X_train,X_test,y_train,y_test = train_test_split(
    X,
    df["doc_type"],
    test_size=0.2
)

model = MultinomialNB()

model.fit(X_train,y_train)
# Predict
predictions = model.predict(X_test)
from sklearn.metrics import accuracy_score
# Accuracy
accuracy = accuracy_score(y_test, predictions)

print("Accuracy:", accuracy)
import joblib
# Save files
joblib.dump(model, "model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("Model saved successfully")
