import streamlit as st
from google import genai
from google.genai import types

st.set_page_config(page_title="Dr. Smith's Clinic Assistant", page_icon=":hospital:")
st.title("Dr. Smith's Clinic Assistant")
st.write("Welcome to Dr. Smith's general practice. How can I help you today?")

if "GEMINI_API_KEY" not in st.secrets:
    st.error("Add GEMINI_API_KEY in .streamlit/secrets.toml or in Streamlit Cloud secrets.")
    st.stop()

client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

sys_instruction = """
You are a helpful and polite clinic receptionist chatbot for Dr. Smith's general practice.
You help patients with:
- Clinic timings (Monday to Saturday, 9 AM to 5 PM)
- Booking appointments
- Basic clinic location information
- Reminding users that you cannot provide official medical diagnoses and they must consult the doctor in person.
"""

if "messages" not in st.session_state:
    st.session_state.messages = []

if "chat" not in st.session_state:
    st.session_state.chat = client.chats.create(
        model="gemini-3.8-flash",
        config=types.GenerateContentConfig(
            system_instruction=sys_instruction,
            temperature=0.3,
        ),
    )

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

user_input = st.chat_input("Type your question here...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    try:
        response = st.session_state.chat.send_message(user_input)
        reply = response.text or "Sorry, I could not generate a reply."
    except Exception as exc:
        reply = f"The clinic assistant could not reach Gemini. Details: {exc}"

    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.write(reply)
