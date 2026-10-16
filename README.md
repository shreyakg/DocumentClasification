# Document Classification Using Machine Learning
## Project Summary

This project is an AI-powered Document Classification System that automatically categorizes business documents into predefined classes such as Invoice, Resume, Contract, and Purchase Order.

The solution combines UiPath for PDF text extraction and Python-based Machine Learning for document classification. Extracted document text is converted into numerical features using TF-IDF Vectorization and classified using a Multinomial Naive Bayes model.

The trained model can classify new documents without retraining and can be integrated into UiPath workflows to automate document processing, routing, and validation. This reduces manual effort, improves accuracy, and increases operational efficiency in document-heavy business environments.
## Project Overview

This project uses Machine Learning and Natural Language Processing (NLP) to automatically classify documents into different categories such as:

- Invoice
- Resume
- Contract
- Purchace Order

The model is trained using text samples and can later be used to classify text extracted from PDF documents.

---

## Business Use Case

Organizations deal with thousands of documents every day. Manually sorting these documents is time-consuming.

This solution automatically identifies the document type and can be integrated with UiPath to automate document routing and processing.

Examples:

| Document | Prediction |
|-----------|------------|
| Invoice Number INV1001 Amount 500 EUR | Invoice |
| Experienced Python Developer | Resume |
| Terms and Conditions Agreement | Contract |

---

## Technologies Used

- Python
- Pandas
- Scikit-Learn
- TF-IDF Vectorization
- Multinomial Naive Bayes
- Joblib
- UiPath

---

## Project Structure

DocumentClassification/

├── documents.xlsx

├── train_model.py

├── predict.py

├── model.pkl

├── vectorizer.pkl

└── README.md

---

## Dataset Structure
The training dataset was generated using UiPath.
The training dataset is stored in Excel format.

### documents.xlsx
Sample PDF Documents
        ↓
UiPath PDF Activities
        ↓
Text Extraction
        ↓
Structured Dataset (Excel)
        ↓
Machine Learning Training

| Text | doc_type |
|---------|----------|
| Invoice Number INV1001 Amount 500 EUR | Invoice |
| Experienced UiPath Developer | Resume |
| Contract Agreement Between Parties | Contract |

### Columns

#### Text
Contains the document content.

#### doc_type
Contains the document category.

---
UiPath was used for:

Reading PDF documents
Extracting document text
Creating the training dataset
Preparing data for Machine Learning

## Machine Learning Pipeline

Text Data

↓

TF-IDF Vectorization

↓

Multinomial Naive Bayes Model

↓

Document Classification

---

## Why TF-IDF?

Machine Learning algorithms cannot understand text directly.

TF-IDF converts text into numerical features by:

- Increasing the importance of significant words.
- Reducing the importance of common words.
- Converting text into vectors that can be processed by ML models.

Example:

Invoice Number Amount

↓

[0.75, 0.41, 0.88]

---

## Why Multinomial Naive Bayes?

Multinomial Naive Bayes is widely used for text classification because:

- Fast training
- Good accuracy on text data
- Works well with TF-IDF features
- Requires small datasets

Common applications:

- Spam Detection
- Sentiment Analysis
- Document Classification

---

## Installation

Install required packages:

```bash
pip install pandas
pip install scikit-learn
pip install openpyxl
pip install joblib
## Future Enhancements
Support additional document types
Train on real-world business documents
Improve OCR accuracy for scanned PDFs
Extract key information (Invoice Number, Vendor Name, Contract Date, etc.)
Deploy as a web application or API for enterprise use
One-Line Resume Description
##Summary
Developed an AI-powered document classification system using UiPath, Python, TF-IDF, and Multinomial Naive Bayes to automatically categorize PDF documents such as invoices, contracts, and resumes with high accuracy.
pip install pypdf 


