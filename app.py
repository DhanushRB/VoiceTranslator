import whisper
from langdetect import detect, DetectorFactory
from googletrans import Translator
from googletrans.constants import LANGUAGES
import sounddevice as sd
import numpy as np
import scipy.io.wavfile

DetectorFactory.seed = 42
translator = Translator()

# Load Whisper large-v3 model
print("Loading whisper-large-v3...")
model = whisper.load_model("large-v3")
print("Model loaded.")

SAMPLE_RATE = 16000
DURATION = 5  # seconds
WAV_FILE = "recorded.wav"

def iso_to_name(code):
    """Convert ISO language code to full language name."""
    return LANGUAGES.get(code.lower(), f"Unknown ({code})").title()

def record_audio(duration=DURATION):
    print(f"\nRecording for {duration} seconds... Speak now.")
    audio = sd.rec(int(duration * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=1, dtype='int16')
    sd.wait()
    scipy.io.wavfile.write(WAV_FILE, SAMPLE_RATE, audio)
    print("Audio recorded and saved.")

def recognize_and_translate(audio_path):
    print("🔍 Transcribing with Whisper...")
    result = model.transcribe(audio_path)
    text = result["text"].strip()
    iso_lang = result["language"]
    lang_name = iso_to_name(iso_lang)

    print(f"Recognized Text: {text}")
    print(f"Detected Language: {lang_name} ({iso_lang})")

    if iso_lang == "en":
        print("ℹ Already in English. No translation needed.")
        return

    try:
        translated = translator.translate(text, dest="en").text
        print(f"Translated: {translated}")
    except Exception as e:
        print(f"Translation error: {e}")

# Loop for continuous input
while True:
    record_audio()
    recognize_and_translate(WAV_FILE)

    user_input = input("\n Do you want to record again? (yes/no): ").strip().lower()
    if user_input not in ["yes", "y"]:
        print(" Goodbye!")
        break
