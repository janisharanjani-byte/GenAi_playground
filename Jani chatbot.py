import truststore
truststore.inject_into_ssl()
import streamlit as st
import ollama
from deep_translator import GoogleTranslator
from langdetect import detect, detect_langs
from gtts import gTTS
from audio_recorder_streamlit import audio_recorder
import speech_recognition as sr
import tempfile

# ==================================
# PAGE CONFIG
# ==================================

st.set_page_config(
    page_title="Multilingual AI Voice Assistant",
    page_icon="🌍",
    layout="wide"
)

st.title("🌍 Multilingual AI Voice Assistant")
st.markdown("Voice + Translation + Ollama AI")

# ==================================
# SPEECH TO TEXT
# ==================================

def speech_to_text(audio_file):

    recognizer = sr.Recognizer()

    try:
        with sr.AudioFile(audio_file) as source:
            audio_data = recognizer.record(source)

        text = recognizer.recognize_google(audio_data)
        return text

    except Exception as e:
        st.error(f"Speech Error: {e}")
        return ""


# ==================================
# TRANSLATE TO ENGLISH
# ==================================

def translate_to_english(text):

    try:

        lang = detect(text)

        st.write("Detected Language:", lang)

        if lang != "en":

            translated = GoogleTranslator(
                source="auto",
                target="en"
            ).translate(text)

            st.write("Translated Text:", translated)

            return translated, lang

        return text, lang

    except Exception as e:

        st.error(f"Translation Error: {e}")

        try:
            lang = detect(text)
            return text, lang

        except Exception:
            return text, "en"

# ==================================
# TRANSLATE BACK
# ==================================

def translate_back(text, target_lang):

    try:

        if target_lang == "en":
            return text

        translated = GoogleTranslator(
            source="en",
            target=target_lang
        ).translate(text)

        return translated

    except Exception as e:

        st.error(f"Translate Back Error: {e}")

        return text
    
GTTS_LANG_MAP = {
    "en": "en",
    "ta": "ta",
    "hi": "hi",
    "te": "te",
    "ml": "ml",
    "kn": "kn",
    "bn": "bn",
    "gu": "gu",
    "mr": "mr"
}

# ==================================
# SENTIMENT ANALYSIS
# ==================================

def get_sentiment(text):

    try:

        response = ollama.chat(
            model="phi3",
            messages=[
                {
                    "role": "user",
                    "content": f"""
Classify the sentiment of this text.

Return ONLY one word:

POSITIVE
NEGATIVE
NEUTRAL

Text:
{text}
"""
                }
            ]
        )

        sentiment = (
            response["message"]["content"]
            .strip()
            .upper()
        )

        return sentiment, 100

    except Exception as e:

        st.error(f"Sentiment Error: {e}")
        return "UNKNOWN", 0


# ==================================
# OLLAMA RESPONSE
# ==================================

def generate_response(prompt):

    try:

        response = ollama.chat(
            model="phi3",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]

    except Exception as e:

        return f"Ollama Error: {e}"


# ==================================
# TEXT TO SPEECH
# ==================================

def text_to_speech(text, language):

    try:

        tts_lang = GTTS_LANG_MAP.get(
            language,
            "en"
        )

        tts = gTTS(
            text=text,
            lang=tts_lang
        )

    except Exception as e:

        st.error(f"TTS Error: {e}")

        tts = gTTS(
            text=text,
            lang="en"
        )

    temp_audio = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".mp3"
    )

    tts.save(temp_audio.name)

    return temp_audio.name

# ==================================
# SESSION STATE
# ==================================

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ==================================
# CLEAR CHAT
# ==================================

if st.button("🗑️ Clear Chat"):

    st.session_state.chat_history = []
    st.rerun()

# ==================================
# TEXT INPUT
# ==================================

user_input = st.text_input(
    "Type your message"
)

# ==================================
# VOICE INPUT
# ==================================

st.subheader("🎤 Speak")

audio_bytes = audio_recorder()

voice_text = ""

if audio_bytes:

    temp_wav = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".wav"
    )

    temp_wav.write(audio_bytes)

    voice_text = speech_to_text(
        temp_wav.name
    )

    if voice_text:
        st.success(
            f"Recognized: {voice_text}"
        )

# ==================================
# FINAL INPUT
# ==================================

final_input = ""

if voice_text:
    final_input = voice_text

elif user_input:
    final_input = user_input

# ==================================
# PROCESS INPUT
# ==================================

send = st.button("Send")
if send and final_input:

    with st.spinner("Thinking..."):

        translated_text, original_lang = (
            translate_to_english(final_input)
        )

        sentiment, score = (
            get_sentiment(translated_text)
        )

        ai_response = (
            generate_response(translated_text)
        )

        final_response = (
            translate_back(
                ai_response,
                original_lang
            )
        )

        st.session_state.chat_history.append(
            ("User", final_input)
        )

        st.session_state.chat_history.append(
            ("AI", final_response)
        )

        # Debug Information

        st.subheader("✅ Analysis")

        st.write(
            f"Detected Language: {original_lang}"
        )

        st.write(
            f"Translated Text: {translated_text}"
        )

        st.write(
            f"Sentiment: {sentiment}"
        )

        st.write(
            f"Confidence: {score}%"
        )

        st.subheader("🤖 AI Response")

        st.write(final_response)

        audio_file = text_to_speech(
        final_response,
        original_lang
        )

        st.audio(audio_file)

# ==================================
# CHAT HISTORY
# ==================================

if st.session_state.chat_history:

    st.subheader("💬 Chat History")

    for role, msg in st.session_state.chat_history:

        if role == "User":

            st.markdown(
                f"🧑 **User:** {msg}"
            )

        else:

            st.markdown(
                f"🤖 **AI:** {msg}"
            )