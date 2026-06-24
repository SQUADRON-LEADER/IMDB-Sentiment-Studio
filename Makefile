# Makefile – developer shortcuts for IMDB Sentiment Studio
# Usage: make <target>
# Note: Windows users can run these commands directly in their shell.

.PHONY: run install lint clean help

## run   : Launch the Streamlit app
run:
	python -m streamlit run streamlit_app.py

## install : Install all Python dependencies
install:
	pip install -r requirements.txt

## lint  : Check code style with flake8
lint:
	flake8 streamlit_app.py utils.py --max-line-length=100

## clean : Remove Python cache directories
clean:
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -name "*.pyc" -delete 2>/dev/null || true

## help  : Print this help message
help:
	@grep -E '^## ' Makefile | sed 's/## /  /'
