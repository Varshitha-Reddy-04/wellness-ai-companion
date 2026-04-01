#!/usr/bin/env bash
pip install -r requirements.txt
python -c "import nltk; nltk.download('punkt_tab')"
uvicorn main:app --host 0.0.0.0 --port ${PORT:-10000}