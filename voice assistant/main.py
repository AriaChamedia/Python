import speech_recognition as sr
import pyttsx3
from googletrans import Translator

# Initialize once (IMPORTANT)
engine = pyttsx3.init()
engine.setProperty('rate', 150)

translator = Translator()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def speech_to_text():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("🎤 Speak now in English...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language="en-US")
        print("✅ You said:", text)
        return text
    except sr.UnknownValueError:
        print("❌ Could not understand")
    except sr.RequestError as e:
        print("❌ API error:", e)
    return ""

def translate_text(text, target_language):
    translated = translator.translate(text, dest=target_language)
    print("🌍 Translation:", translated.text)
    return translated.text

def choose_language():
    print("\n🌍 Choose language:")
    print("1. Hindi")
    print("2. Tamil")
    print("3. Telugu")
    print("4. Bengali")
    print("5. Marathi")
    print("6. Gujarati")
    print("7. Malayalam")
    print("8. Punjabi")

    choice = input("Enter number (1–8): ")

    languages = {
        "1": "hi", "2": "ta", "3": "te", "4": "bn",
        "5": "mr", "6": "gu", "7": "ml", "8": "pa"
    }

    return languages.get(choice, "hi")

def main():
    target_language = choose_language()
    text = speech_to_text()

    if text:
        translated = translate_text(text, target_language)
        speak(translated)
        print("🔊 Done!")

main()
