# Fake News Detection System

## Overview

This project implements a Fake News Detection System using Machine Learning and Natural Language Processing (NLP).
The system analyzes news text and classifies it as Real or Fake, and also provides a brief explanation for the prediction.

The model is exposed as a Flask REST API and containerized using Docker for portability and ease of deployment.

---

## Features

* Machine learning-based text classification (Real / Fake)
* NLP preprocessing (tokenization, stopword removal)
* TF-IDF feature extraction
* Fast inference using Naive Bayes
* Explanation for each prediction
* REST API using Flask
* Dockerized deployment

---

## Tech Stack

* Python
* scikit-learn
* NLTK
* Flask
* Docker

---

## Project Structure

```
Fake-News-Detective/
│
├── app.py                         # Flask API
├── model.pkl                      # Trained ML model
├── test.py                        # API testing script
├── requirements.txt               # Dependencies
├── Dockerfile                     # Docker configuration
├── README.md                      # Project documentation
└── Fake_News_Detection_Paper.pdf  # Research paper
```

---

## How It Works

1. Input news text
2. Preprocessing (cleaning, tokenization, stopword removal)
3. Text is converted into numerical features using TF-IDF
4. Model predicts Real or Fake
5. System returns prediction and explanation

---

## Running the Project

### Run Locally

```
pip install -r requirements.txt
python app.py
```

---

### Run with Docker

```
docker build -t fake-news-app .
docker run -p 5000:5000 fake-news-app
```

---

## API Usage

### Endpoint

```
POST /predict
```

### Example Request

```
{
  "text": "Aliens officially join Indian parliament"
}
```

### Example Response

```
{
  "prediction": 0,
  "explanation": "This news may be fake due to exaggerated or misleading content."
}
```

---

## Results

* Accuracy: approximately 94%
* Fast response time (<150 ms)
* Consistent performance on unseen data

---

## Research Paper

The complete research paper is included in this repository:
Fake_News_Detection_Paper.pdf

---

## Future Work

* Improve performance using deep learning models (LSTM, BERT)
* Enhance explanation using advanced AI techniques
* Add a web-based user interface
* Support multiple languages

---

## Author

Kirutikaa G

---

## License

This project is intended for academic and educational purposes.
