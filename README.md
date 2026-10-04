# Dr. Smith's Clinic Assistant

Final Streamlit receptionist chatbot. Model: `gemini-3.8-flash`.

Repo: https://github.com/kmukesh1/clinic-assistant

## Requirements

```text
streamlit
google-genai
```

## Secret (do not commit)

Local file `.streamlit/secrets.toml`:

```toml
GEMINI_API_KEY = "your-key-here"
```

Streamlit Cloud: App settings → Secrets, paste the same line.

## Run

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy

1. https://share.streamlit.io
2. Repository: `kmukesh1/clinic-assistant`
3. Branch: `main`
4. Main file: `app.py`
5. Add `GEMINI_API_KEY` in Secrets, then Deploy.
