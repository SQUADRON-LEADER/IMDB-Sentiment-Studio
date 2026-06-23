import streamlit as st
import torch
import torch.nn as nn
import joblib
import numpy as np
from pathlib import Path

st.set_page_config(
    page_title="IMDB Sentiment Studio",
    page_icon="🎬",
    layout="centered"
)

# ─── Model Definition ──────────────────────────────────────────────────────────

BASE_DIR = Path(__file__).parent

class RNNModel(nn.Module):
    """
    Architecture matches the saved checkpoint exactly:
      - RNN layer named 'RNNModel' (as it was during training)
      - fc outputs 2 classes (negative=0, positive=1)
    """
    def __init__(self, input_size=5000, hidden_size=128, num_layers=1):
        super(RNNModel, self).__init__()
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        # NOTE: must be named 'RNNModel' to match saved state_dict keys
        self.RNNModel = nn.RNN(input_size, hidden_size, num_layers, batch_first=True)
        self.fc = nn.Linear(hidden_size, 2)  # 2-class output

    def forward(self, x):
        h0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size)
        out, _ = self.RNNModel(x, h0)
        out = self.fc(out[:, -1, :])
        return out  # raw logits; softmax applied in predict_sentiment


@st.cache_resource
def load_artifacts():
    """Load and cache model, vectorizer, and label encoder from disk."""
    vectorizer = joblib.load(BASE_DIR / "tfidf_vectorizer.pkl")
    label_encoder = joblib.load(BASE_DIR / "label_encoder.pkl")

    model = RNNModel(input_size=5000, hidden_size=128, num_layers=1)
    state_dict = torch.load(
        BASE_DIR / "rnn_model_state.pt",
        map_location=torch.device("cpu"),
        weights_only=True
    )
    model.load_state_dict(state_dict)
    model.eval()
    return model, vectorizer, label_encoder


def predict_sentiment(review: str):
    """
    Transform a raw review string and run inference.
    Returns: (label, confidence, score_map)
    """
    model, vectorizer, label_encoder = load_artifacts()

    # TF-IDF → dense numpy array, shape (1, 5000)
    tfidf_vec = vectorizer.transform([review])
    dense = tfidf_vec.toarray().astype(np.float32)
    # Model expects (batch, seq_len, input_size) → unsqueeze seq_len dim
    tensor_input = torch.tensor(dense).unsqueeze(1)          # shape (1, 1, 5000)

    with torch.no_grad():
        logits = model(tensor_input)                          # shape (1, 2)
        probs = torch.softmax(logits, dim=1).squeeze()       # shape (2,)

    classes = list(label_encoder.classes_)                   # ['negative', 'positive'] or similar
    prob_values = probs.numpy()                              # [prob_class0, prob_class1]

    predicted_idx = int(np.argmax(prob_values))
    label = classes[predicted_idx]
    confidence = float(prob_values[predicted_idx])

    score_map = {cls: float(prob_values[i]) for i, cls in enumerate(classes)}
    return label, confidence, score_map


# ─── CSS ───────────────────────────────────────────────────────────────────────

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');

* { font-family: 'Inter', sans-serif; }

.stApp {
    background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 50%, #0f172a 100%);
}

.main .block-container {
    max-width: 900px;
    padding-top: 2rem;
    padding-bottom: 2rem;
}

h1 { text-align: center; color: white; }

.subtitle {
    text-align: center;
    color: #94a3b8;
    font-size: 18px;
    margin-bottom: 30px;
}

/* Text area */
.stTextArea textarea {
    background: #111827 !important;
    color: white !important;
    border: 2px solid #334155 !important;
    border-radius: 20px !important;
    padding: 20px !important;
    font-size: 18px !important;
}
.stTextArea textarea:focus {
    border: 2px solid #6366f1 !important;
    box-shadow: 0 0 20px rgba(99,102,241,0.4) !important;
}
.stTextArea label {
    color: #e2e8f0 !important;
    font-size: 16px !important;
    font-weight: 600 !important;
}

/* Buttons */
.stButton button {
    height: 50px;
    border-radius: 15px !important;
    font-size: 17px !important;
    font-weight: 600 !important;
    transition: all 0.2s ease !important;
}
.stButton button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 20px rgba(99,102,241,0.4) !important;
}

/* Result card */
.result-card {
    background: linear-gradient(135deg, #1e1b4b, #111827);
    padding: 30px;
    border-radius: 25px;
    margin-top: 30px;
    border: 1px solid #4338ca;
    box-shadow: 0 0 30px rgba(99,102,241,0.2);
    animation: fadeIn 0.5s ease;
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(10px); }
    to   { opacity: 1; transform: translateY(0); }
}

/* Progress bar label */
p { color: #e2e8f0 !important; }
</style>
""", unsafe_allow_html=True)

# ─── Header ────────────────────────────────────────────────────────────────────

st.markdown("""
<h1>🎬 IMDB Sentiment Studio</h1>
<div class='subtitle'>AI Powered Movie Review Sentiment Analyzer</div>
""", unsafe_allow_html=True)

# ─── Sample Reviews ────────────────────────────────────────────────────────────

sample_positive = "A beautifully acted film with heartfelt moments and brilliant direction."
sample_negative = "Despite a strong cast, it was boring, messy, and way too long."

# ─── Session State ─────────────────────────────────────────────────────────────

if "review_text" not in st.session_state:
    st.session_state.review_text = ""

if "auto_analyze" not in st.session_state:
    st.session_state.auto_analyze = False


def select_sample(text):
    st.session_state.review_text = text
    st.session_state.auto_analyze = True


# ─── Text Area ─────────────────────────────────────────────────────────────────

review = st.text_area(
    "✍️ Enter Movie Review",
    placeholder="Type a movie review here...",
    height=180,
    key="review_text"
)

# ─── Sample Buttons ────────────────────────────────────────────────────────────

c1, c2 = st.columns(2)
with c1:
    st.button("✨ Positive Sample", use_container_width=True,
              on_click=select_sample, args=(sample_positive,))
with c2:
    st.button("⚡ Negative Sample", use_container_width=True,
              on_click=select_sample, args=(sample_negative,))

# ─── Analyze Button ────────────────────────────────────────────────────────────

analyze = st.button("🚀 Analyze Sentiment", type="primary", use_container_width=True)

# ─── Prediction ────────────────────────────────────────────────────────────────

if analyze or st.session_state.auto_analyze:
    st.session_state.auto_analyze = False

    if not review.strip():
        st.warning("⚠️ Please enter a movie review first.")
    else:
        with st.spinner("Analyzing sentiment..."):
            try:
                label, confidence, score_map = predict_sentiment(review)

                if label.lower() == "positive":
                    emoji = "😊"
                    color = "#10b981"
                    glow = "rgba(16,185,129,0.3)"
                else:
                    emoji = "😔"
                    color = "#ef4444"
                    glow = "rgba(239,68,68,0.3)"

                st.markdown(f"""
<div class='result-card' style='border-color:{color};box-shadow:0 0 30px {glow};'>
  <h3 style='color:#94a3b8;margin:0 0 10px 0;'>Prediction Result</h3>
  <h1 style='color:{color};margin:0;font-size:48px;text-align:center;'>
    {emoji} {label.upper()}
  </h1>
  <h2 style='text-align:center;color:white;margin:10px 0 0 0;'>
    {confidence*100:.1f}% Confidence
  </h2>
</div>
""", unsafe_allow_html=True)

                st.write("")
                st.subheader("📊 Class Probabilities")
                for cls, prob in score_map.items():
                    bar_color = "#10b981" if cls.lower() == "positive" else "#ef4444"
                    st.markdown(f"**{cls.title()}** — `{prob*100:.2f}%`")
                    st.progress(float(prob))

            except Exception as e:
                st.error(f"❌ Error during prediction: {e}")
                st.info("Make sure `rnn_model_state.pt`, `tfidf_vectorizer.pkl`, and `label_encoder.pkl` exist in the same folder as `streamlit_app.py`.")