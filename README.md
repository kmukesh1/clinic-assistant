# Dr. Smith's Clinic Assistant

Streamlit receptionist chatbot for a general practice. It uses the Gemini API (`gemini-3.8-flash`).

Repo: https://github.com/kmukesh1/clinic-assistant

## Run on your computer

```bash
pip install -r requirements.txt
mkdir -p .streamlit
cp .streamlit/secrets.toml.example .streamlit/secrets.toml
```

Edit `.streamlit/secrets.toml` and paste a key from https://aistudio.google.com/apikey

```bash
streamlit run app.py
```

## Deploy on Streamlit Community Cloud

1. Push this repo (already on GitHub).
2. Go to https://share.streamlit.io and create an app from `kmukesh1/clinic-assistant`, file `app.py`.
3. In Advanced settings → Secrets, paste:

```toml
GEMINI_API_KEY = "your-key"
```

Do not commit the real key.

## What it does

- Clinic hours: Monday to Saturday, 9 AM to 5 PM
- Appointment requests and location questions
- Reminds the user it cannot give a medical diagnosis
