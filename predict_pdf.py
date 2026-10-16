import os
import joblib

from pypdf import PdfReader

model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

folder = "C:\\Users\\shreya.gurikar\\Desktop\\Dev_course\\DocumentClassification\\synthetic_document_pack_80_pdfs\\Testdata"

for file in os.listdir(folder):

    if file.endswith(".pdf"):

        pdf_path = os.path.join(folder, file)

        text = ""

        reader = PdfReader(pdf_path)

        for page in reader.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text

        vector = vectorizer.transform([text])

        prediction = model.predict(vector)

        print(file, "->", prediction[0])