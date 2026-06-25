# 🎬 IMDB Sentiment Studio

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Streamlit-1.35+-FF4B4B?logo=streamlit&logoColor=white" alt="Streamlit">
  <img src="https://img.shields.io/badge/PyTorch-2.3+-EE4C2C?logo=pytorch&logoColor=white" alt="PyTorch">
  <img src="https://img.shields.io/badge/scikit--learn-TF--IDF-F7931E?logo=scikitlearn&logoColor=white" alt="Scikit Learn">
  <img src="https://img.shields.io/badge/License-MIT-green" alt="MIT License">
  <img src="https://img.shields.io/github/actions/workflow/status/SQUADRON-LEADER/IMDB-Sentiment-Studio/ci.yml?label=CI" alt="CI Status">
</p>

<p align="center">
  <b>An elegant AI-powered Sentiment Analysis application built with <b>PyTorch</b> and <b>Streamlit</b>.</b><br>
  Analyze IMDB movie reviews in real time using a trained Recurrent Neural Network (RNN) and an optimized TF-IDF vectorizer.
</p>

---

# 🌟 Overview

**IMDB Sentiment Studio** is a modern NLP application that predicts whether a movie review expresses a **Positive 😊** or **Negative 😞** sentiment.

Designed with a sleek **glassmorphism-inspired interface**, the application combines an intuitive user experience with a powerful deep learning backend, making sentiment analysis both interactive and visually appealing.

Whether you're exploring Natural Language Processing, learning PyTorch, or showcasing an AI deployment project, this repository demonstrates an end-to-end machine learning workflow—from preprocessing text to deploying a trained model as a web application.

---

# 📸 Application Screenshots

> Replace these placeholder paths with your own screenshots.

## 🏠 Home Page

```
assets/home.png
```

![Home](assets/home.png)

---

## ✍️ Entering a Review

```
assets/input.png
```

![Input](assets/input.png)

---

## 📊 Prediction Result

```
assets/prediction.png
```

![Prediction](assets/prediction.png)

---

## 📈 Confidence Scores

```
assets/confidence.png
```

![Confidence](assets/confidence.png)

---

## 🕒 Prediction History

```
assets/history.png
```

![History](assets/history.png)

---

# 🎥 Demo

> Add a GIF to showcase the application's workflow.

```
assets/demo.gif
```

![Demo](assets/demo.gif)

---

# ✨ Features

| Feature                    | Description                                            |
| -------------------------- | ------------------------------------------------------ |
| 🤖 Deep Learning Inference | Predicts sentiment using a trained PyTorch RNN         |
| 📝 Live Text Statistics    | Character count and word count while typing            |
| 📊 Confidence Scores       | Displays prediction probabilities for both classes     |
| 📚 Prediction History      | Stores previous predictions during the current session |
| ⚡ Instant Predictions      | Fast inference using a TF-IDF vectorizer               |
| 🎨 Modern UI               | Glassmorphism-inspired interface with gradients        |
| 🌙 Dark Theme              | Native Streamlit dark theme                            |
| 🧪 Sample Reviews          | One-click positive and negative examples               |
| 🧹 Modular Codebase        | Organized utilities and reusable functions             |
| ✅ Unit Tested              | Includes automated PyTest test suite                   |
| 🚀 GitHub Actions          | Continuous Integration support                         |

---

# 🛠️ Tech Stack

| Category             | Technology     |
| -------------------- | -------------- |
| Programming Language | Python         |
| Deep Learning        | PyTorch        |
| Machine Learning     | Scikit-Learn   |
| NLP                  | TF-IDF         |
| Web Framework        | Streamlit      |
| Testing              | PyTest         |
| CI/CD                | GitHub Actions |
| Version Control      | Git + GitHub   |

---

# ⚙️ How It Works

```
User Review
      │
      ▼
Text Cleaning
      │
      ▼
TF-IDF Vectorization
      │
      ▼
PyTorch RNN
      │
      ▼
Softmax Probabilities
      │
      ▼
Positive / Negative Prediction
      │
      ▼
Displayed in Beautiful Streamlit UI
```

---

# 📦 Installation

```bash
# Clone repository
git clone https://github.com/SQUADRON-LEADER/IMDB-Sentiment-Studio.git

cd IMDB-Sentiment-Studio

# Create virtual environment (Optional)
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Git LFS

The dataset exceeds GitHub's upload limit.

Install Git LFS:

```bash
git lfs install
git lfs pull
```

---

# 🚀 Running the Application

```bash
python -m streamlit run streamlit_app.py
```

or

```bash
make run
```

Open

```
http://localhost:8501
```

---

# 📊 Sample Prediction

### Input

```
The acting was incredible and the story kept me engaged from beginning to end.
```

### Output

```
Prediction

Positive 😊

Confidence

Positive : 97.82%

Negative : 2.18%
```

---

# 🧠 Model Details

| Property        | Value                 |
| --------------- | --------------------- |
| Model           | PyTorch RNN           |
| Hidden Units    | 128                   |
| Vocabulary Size | 5000                  |
| Classes         | Positive / Negative   |
| Dataset Size    | 50,000 Reviews        |
| Output          | Binary Classification |

---

# 💾 Saved Model Files

| File                  | Description           |
| --------------------- | --------------------- |
| rnn_model_state.pt    | Trained model weights |
| tfidf_vectorizer.pkl  | TF-IDF Vectorizer     |
| label_encoder.pkl     | Label Encoder         |
| rnn_model_config.json | Hyperparameters       |

---

# 📂 Project Structure

```text
IMDB-Sentiment-Studio
│
├── .github/
│   ├── workflows/
│   │   └── ci.yml
│   └── ISSUE_TEMPLATE/
│
├── .streamlit/
│   └── config.toml
│
├── assets/
│   ├── banner.png
│   ├── home.png
│   ├── input.png
│   ├── prediction.png
│   ├── confidence.png
│   ├── history.png
│   └── demo.gif
│
├── tests/
│   └── test_utils.py
│
├── streamlit_app.py
├── utils.py
├── requirements.txt
├── Makefile
├── rnn_model_state.pt
├── tfidf_vectorizer.pkl
├── label_encoder.pkl
├── rnn_model_config.json
├── IMDB Dataset.csv
├── CONTRIBUTING.md
├── CHANGELOG.md
├── LICENSE
└── README.md
```

---

# 🧪 Running Tests

```bash
pip install pytest

pytest tests/ -v
```

---

# 📈 Project Highlights

* End-to-End NLP Pipeline
* Real-Time Deep Learning Inference
* Beautiful Glassmorphism UI
* Confidence Score Visualization
* Prediction History
* Modular Python Architecture
* Automated Unit Tests
* GitHub Actions Integration
* Easy Deployment
* Beginner Friendly

---

# 🗺️ Roadmap

* [ ] LSTM Support
* [ ] GRU Model
* [ ] Transformer (BERT)
* [ ] Docker Deployment
* [ ] HuggingFace Integration
* [ ] Multi-language Sentiment Analysis
* [ ] Explainable AI (SHAP)
* [ ] Export Prediction History

---

# 🤝 Contributing

Contributions are always welcome!

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Push the branch.
5. Open a Pull Request.

---

# 📜 License

This project is licensed under the **MIT License**.

Feel free to use, modify, and distribute this project under the terms of the license.

---

# ⭐ Support

If you found this project useful:

⭐ Star the repository

🍴 Fork the repository

🐛 Report issues

💡 Suggest new features

Your support helps improve the project and motivates future development.

---

<p align="center">

### 🎬 Built with ❤️ using Python, PyTorch & Streamlit

**If you like this project, don't forget to ⭐ star the repository!**

</p>
