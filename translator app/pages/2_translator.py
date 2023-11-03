import streamlit as st
import googletrans
import speech_recognition as sr
from gtts import gTTS
from io import BytesIO

st.set_page_config(
    page_title="TranslateMate"
) 
st.title("Translator and Interpreter")
lang=googletrans.LANGUAGES
user_input = st.text_input("Enter text:")
language = st.selectbox("Target Language",lang.values())



if st.button("Translate"):
    translator=googletrans.Translator()
    translation = translator.translate(user_input,dest=language)
    user_output = st.text_area("target",translation.text)
    if user_output:
        # Convert the text to speech
        tts = gTTS(user_output)
        speech = BytesIO()
        tts.write_to_fp(speech)
        st.audio(speech, format="audio/wav")

        
st.sidebar.success("Select from above")