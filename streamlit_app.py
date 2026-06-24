"""
streamlit_app.py – IMDB Sentiment Studio
=========================================
Main Streamlit entry-point. Inference logic lives in utils.py.
"""

import streamlit as st

from utils import load_artifacts, predict_sentiment, text_stats

# ─── Page Config ──────────────────────────────────────────────────────────────

st.set_page_config(
    page_title="IMDB Sentiment Studio",
    page_icon="🎬",
    layout="centered",
)

# ─── CSS ──────────────────────────────────────────────────────────────────────

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

/* Stats badge */
.stats-badge {
    display: inline-block;
    background: #1e293b;
    border: 1px solid #334155;
    border-radius: 8px;
    padding: 4px 12px;
    color: #94a3b8;
    font-size: 13px;
    margin-right: 8px;
}

/* Progress bar label */
p { color: #e2e8f0 !important; }
</style>
""", unsafe_allow_html=True)

# ─── Header ───────────────────────────────────────────────────────────────────

st.markdown("""
<h1>🎬 IMDB Sentiment Studio</h1>
<div class='subtitle'>AI Powered Movie Review Sentiment Analyzer</div>
""", unsafe_allow_html=True)

# ─── Sample Reviews ───────────────────────────────────────────────────────────

SAMPLE_POSITIVE = "A beautifully acted film with heartfelt moments and brilliant direction."
SAMPLE_NEGATIVE = "Despite a strong cast, it was boring, messy, and way too long."

# ─── Session State ────────────────────────────────────────────────────────────

if "review_text" not in st.session_state:
    st.session_state.review_text = ""
if "auto_analyze" not in st.session_state:
    st.session_state.auto_analyze = False
if "history" not in st.session_state:
    st.session_state.history = []


def select_sample(text: str) -> None:
    st.session_state.review_text = text
    st.session_state.auto_analyze = True


# ─── Text Area ────────────────────────────────────────────────────────────────

review = st.text_area(
    "✍️ Enter Movie Review",
    placeholder="Type a movie review here...",
    height=180,
    key="review_text",
)

# ─── Text Stats ───────────────────────────────────────────────────────────────

stats = text_stats(review)
st.markdown(
    f"<span class='stats-badge'>📝 {stats['word_count']} words</span>"
    f"<span class='stats-badge'>🔤 {stats['char_count']} characters</span>",
    unsafe_allow_html=True,
)

st.write("")

# ─── Sample Buttons ───────────────────────────────────────────────────────────

c1, c2 = st.columns(2)
with c1:
    st.button("✨ Positive Sample", use_container_width=True,
              on_click=select_sample, args=(SAMPLE_POSITIVE,))
with c2:
    st.button("⚡ Negative Sample", use_container_width=True,
              on_click=select_sample, args=(SAMPLE_NEGATIVE,))

# ─── Analyze Button ───────────────────────────────────────────────────────────

analyze = st.button("🚀 Analyze Sentiment", type="primary", use_container_width=True)

# ─── Prediction ───────────────────────────────────────────────────────────────

if analyze or st.session_state.auto_analyze:
    st.session_state.auto_analyze = False

    if not review.strip():
        st.warning("⚠️ Please enter a movie review first.")
    else:
        with st.spinner("Analyzing sentiment…"):
            try:
                label, confidence, score_map = predict_sentiment(review)

                if label.lower() == "positive":
                    emoji, color, glow = "😊", "#10b981", "rgba(16,185,129,0.3)"
                else:
                    emoji, color, glow = "😔", "#ef4444", "rgba(239,68,68,0.3)"

                # Store in history
                st.session_state.history.append({
                    "review": review[:80] + ("…" if len(review) > 80 else ""),
                    "label": label,
                    "confidence": confidence,
                })

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
                    st.markdown(f"**{cls.title()}** — `{prob*100:.2f}%`")
                    st.progress(float(prob))

            except FileNotFoundError as exc:
                st.error(f"❌ Missing artefact: {exc.filename}")
                st.info(
                    "Make sure `rnn_model_state.pt`, `tfidf_vectorizer.pkl`, and "
                    "`label_encoder.pkl` exist in the same folder as `streamlit_app.py`."
                )
            except Exception as exc:
                st.error(f"❌ Unexpected error: {exc}")

# ─── Prediction History ───────────────────────────────────────────────────────

if st.session_state.history:
    st.write("")
    with st.expander("🕑 Prediction History", expanded=False):
        for i, entry in enumerate(reversed(st.session_state.history), 1):
            icon = "😊" if entry["label"].lower() == "positive" else "😔"
            st.markdown(
                f"**{i}.** {icon} `{entry['label'].upper()}` "
                f"({entry['confidence']*100:.1f}%) — *{entry['review']}*"
            )

# ─── Sidebar ──────────────────────────────────────────────────────────────────

with st.sidebar:
    st.markdown("## 🎬 About")
    st.markdown(
        "**IMDB Sentiment Studio** uses a single-layer PyTorch RNN trained on "
        "50 000 IMDB reviews to classify text as **Positive** or **Negative**."
    )
    st.markdown("---")
    st.markdown("### 🧠 Model Info")
    st.markdown("- **Architecture**: RNN (1 layer, 128 hidden units)")
    st.markdown("- **Features**: TF-IDF (5 000 vocab)")
    st.markdown("- **Classes**: Negative / Positive")
    st.markdown("---")
    st.markdown(
        "[![GitHub](https://img.shields.io/badge/GitHub-Repo-181717?logo=github)]"
        "(https://github.com/SQUADRON-LEADER/IMDB-Sentiment-Studio)"
    )

    # Warm up model silently
    load_artifacts()