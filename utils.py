"""
utils.py – shared helpers for IMDB Sentiment Studio
=====================================================
Contains:
  - RNNModel  : PyTorch model class (must match training checkpoint)
  - load_artifacts  : cached loader for model + vectorizer + label encoder
  - predict_sentiment : end-to-end inference pipeline
  - clean_text : lightweight text pre-processing utility
"""

from pathlib import Path

import joblib
import numpy as np
import streamlit as st
import torch
import torch.nn as nn

BASE_DIR = Path(__file__).parent


# ── Model Architecture ────────────────────────────────────────────────────────

class RNNModel(nn.Module):
    """
    Single-layer RNN sentiment classifier.

    Architecture:
        Input  : TF-IDF dense vector of shape (batch, 1, input_size)
        RNN    : nn.RNN with hidden_size units
        Output : 2 logits (negative=0, positive=1)

    The internal layer **must** be named ``RNNModel`` to match the
    keys saved in ``rnn_model_state.pt``.
    """

    def __init__(
        self,
        input_size: int = 5000,
        hidden_size: int = 128,
        num_layers: int = 1,
    ) -> None:
        super().__init__()
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        # Layer name intentionally matches the saved state_dict keys
        self.RNNModel = nn.RNN(
            input_size, hidden_size, num_layers, batch_first=True
        )
        self.fc = nn.Linear(hidden_size, 2)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        h0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size)
        out, _ = self.RNNModel(x, h0)
        return self.fc(out[:, -1, :])  # raw logits


# ── Artifact Loader ───────────────────────────────────────────────────────────

@st.cache_resource(show_spinner=False)
def load_artifacts():
    """
    Load and cache the TF-IDF vectorizer, label encoder, and RNN model.

    Returns
    -------
    tuple[RNNModel, TfidfVectorizer, LabelEncoder]
    """
    vectorizer = joblib.load(BASE_DIR / "tfidf_vectorizer.pkl")
    label_encoder = joblib.load(BASE_DIR / "label_encoder.pkl")

    model = RNNModel(input_size=5000, hidden_size=128, num_layers=1)
    state = torch.load(
        BASE_DIR / "rnn_model_state.pt",
        map_location=torch.device("cpu"),
        weights_only=True,
    )
    model.load_state_dict(state)
    model.eval()
    return model, vectorizer, label_encoder


# ── Inference ─────────────────────────────────────────────────────────────────

def predict_sentiment(review: str) -> tuple[str, float, dict[str, float]]:
    """
    Run sentiment inference on a raw review string.

    Parameters
    ----------
    review : str
        Raw movie review text.

    Returns
    -------
    label : str
        Predicted class label (e.g. ``"positive"`` or ``"negative"``).
    confidence : float
        Probability of the predicted class (0–1).
    score_map : dict[str, float]
        Mapping of every class label to its probability.
    """
    model, vectorizer, label_encoder = load_artifacts()

    tfidf_vec = vectorizer.transform([review])
    dense = tfidf_vec.toarray().astype(np.float32)
    tensor_input = torch.tensor(dense).unsqueeze(1)  # (1, 1, 5000)

    with torch.no_grad():
        logits = model(tensor_input)                         # (1, 2)
        probs = torch.softmax(logits, dim=1).squeeze()      # (2,)

    classes: list[str] = list(label_encoder.classes_)
    prob_values: np.ndarray = probs.numpy()

    predicted_idx = int(np.argmax(prob_values))
    label = classes[predicted_idx]
    confidence = float(prob_values[predicted_idx])
    score_map = {cls: float(prob_values[i]) for i, cls in enumerate(classes)}

    return label, confidence, score_map


# ── Text Utilities ────────────────────────────────────────────────────────────

def text_stats(text: str) -> dict[str, int]:
    """
    Return basic statistics about a piece of text.

    Parameters
    ----------
    text : str
        Input text.

    Returns
    -------
    dict with keys ``word_count`` and ``char_count``.
    """
    stripped = text.strip()
    return {
        "word_count": len(stripped.split()) if stripped else 0,
        "char_count": len(stripped),
    }
