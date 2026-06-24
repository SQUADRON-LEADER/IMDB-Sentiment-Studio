# Changelog

All notable changes to **IMDB Sentiment Studio** are documented here.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]

### Planned
- LSTM / GRU model variant support
- Batch analysis mode (upload a CSV)
- Exportable prediction history

---

## [1.1.0] - 2025-06-24

### Added
- Sidebar **About** section with model and project info
- **Prediction history** panel (session-scoped)
- Word count and character count display beneath the text area
- `utils.py` helper module (model loading, prediction logic)
- `CONTRIBUTING.md`, `CHANGELOG.md`, `LICENSE`
- `.gitignore` for Python/PyTorch/Streamlit projects
- Pinned minimum versions in `requirements.txt`
- Expanded `rnn_model_config.json` with architecture metadata

### Changed
- Refactored `streamlit_app.py` to import from `utils.py`
- Improved error messages with actionable hints

---

## [1.0.0] - 2025-06-20

### Added
- Initial Streamlit app with RNN sentiment analysis
- Dark-themed glassmorphic UI
- Positive / Negative sample review buttons
- Class probability progress bars
- TF-IDF + PyTorch RNN inference pipeline
