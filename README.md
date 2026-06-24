# 🎬 IMDB Sentiment Studio

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Streamlit-1.35+-FF4B4B?logo=streamlit&logoColor=white" alt="Streamlit">
  <img src="https://img.shields.io/badge/PyTorch-2.3+-EE4C2C?logo=pytorch&logoColor=white" alt="PyTorch">
  <img src="https://img.shields.io/badge/License-MIT-green" alt="MIT License">
  <img src="https://img.shields.io/github/actions/workflow/status/SQUADRON-LEADER/IMDB-Sentiment-Studio/ci.yml?label=CI" alt="CI Status">
</p>

A **dark‑themed**, glassmorphic Streamlit web app that performs real-time sentiment analysis on IMDB movie reviews using a pre‑trained **PyTorch RNN** model and a **TF‑IDF** vectorizer.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🤖 **RNN Inference** | Single-layer PyTorch RNN trained on 50 000 IMDB reviews |
| 📊 **Probability Breakdown** | Per-class confidence with visual progress bars |
| 🕑 **Prediction History** | Session-scoped history panel for all past predictions |
| 📝 **Text Stats** | Live word and character count as you type |
| 🎨 **Rich UI** | Gradient background, glassmorphic cards, smooth animations |
| ⚡ **Sample Reviews** | One-click positive / negative examples for quick demos |
| 🌙 **Dark Theme** | Native Streamlit dark theme via `.streamlit/config.toml` |

---

## 📦 Installation

```bash
# Clone the repo
git clone https://github.com/SQUADRON-LEADER/IMDB-Sentiment-Studio.git
cd IMDB-Sentiment-Studio

# (Optional) Create a virtual environment
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

> **Note**: The dataset file (`IMDB Dataset.csv`) exceeds GitHub's 50 MB limit and is stored with **Git LFS**. Install Git LFS if you need the raw data:
> ```bash
> git lfs install
> git lfs pull
> ```

---

## 🚀 Running the App

```bash
python -m streamlit run streamlit_app.py
# or using make:
make run
```

The app will be available at `http://localhost:8501`.

---

## 🧪 Running Tests

```bash
pip install pytest
pytest tests/ -v
```

---

## 🧠 Model Details

- **Architecture**: Single‑layer `nn.RNN` — 5 000 input features, 128 hidden units, 2-class output
- **Training data**: 50 000 IMDB movie reviews (balanced binary sentiment)
- **Vectorizer**: scikit‑learn TF‑IDF (5 000 vocab size)

### Saved Artefacts

| File | Description |
|---|---|
| `rnn_model_state.pt` | Trained model weights |
| `tfidf_vectorizer.pkl` | Fitted TF‑IDF vectorizer |
| `label_encoder.pkl` | Label encoder (`negative` / `positive`) |
| `rnn_model_config.json` | Hyperparameter metadata |

---

## 📂 Repository Structure

```
IMDB-Sentiment-Studio/
├── streamlit_app.py          # Streamlit UI entry point
├── utils.py                  # Model class, loader, inference, text helpers
├── rnn_model_config.json     # Model hyperparameters
├── rnn_model_state.pt        # Trained weights
├── tfidf_vectorizer.pkl      # TF-IDF vectorizer
├── label_encoder.pkl         # Label encoder
├── requirements.txt          # Python dependencies
├── Makefile                  # Developer shortcuts
├── IMDB Dataset.csv          # Raw dataset (Git LFS)
├── tests/
│   └── test_utils.py         # pytest unit tests
├── .streamlit/
│   └── config.toml           # Dark theme configuration
├── .github/
│   ├── workflows/ci.yml      # GitHub Actions CI
│   └── ISSUE_TEMPLATE/       # Bug report & feature request templates
├── CONTRIBUTING.md
├── CHANGELOG.md
├── LICENSE
└── README.md
```

---

## 🛠️ Development & Contributions

See [CONTRIBUTING.md](CONTRIBUTING.md) for setup, coding style, and PR guidelines.

---

## 📜 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.
