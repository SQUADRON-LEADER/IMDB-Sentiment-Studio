# Contributing to IMDB Sentiment Studio

Thank you for considering contributing! 🎉

## Getting Started

1. **Fork** this repository.
2. **Clone** your fork locally:
   ```bash
   git clone https://github.com/<your-username>/IMDB-Sentiment-Studio.git
   cd IMDB-Sentiment-Studio
   ```
3. **Create a branch** for your feature or fix:
   ```bash
   git checkout -b feature/your-feature-name
   ```
4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Development Guidelines

- Follow [PEP 8](https://pep8.org/) for Python code style.
- Keep functions small and well-documented with docstrings.
- Do **not** commit large binary files (model weights, datasets) without Git LFS.
- Test your changes locally with:
  ```bash
  python -m streamlit run streamlit_app.py
  ```

## Commit Message Convention

Use the [Conventional Commits](https://www.conventionalcommits.org/) format:

| Prefix     | Use for                                    |
|------------|--------------------------------------------|
| `feat:`    | New feature                                |
| `fix:`     | Bug fix                                    |
| `docs:`    | Documentation changes                      |
| `style:`   | Formatting / whitespace (no logic change)  |
| `refactor:`| Code restructuring (no feature / bug)      |
| `chore:`   | Build, deps, config changes                |

## Submitting a Pull Request

1. Push your branch: `git push origin feature/your-feature-name`
2. Open a Pull Request against `main`.
3. Fill in the PR template and link any relevant issues.
4. Wait for review — we aim to respond within 48 hours.

## Code of Conduct

Be respectful, inclusive, and constructive. We follow the [Contributor Covenant](https://www.contributor-covenant.org/).
