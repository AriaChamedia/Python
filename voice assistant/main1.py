# This library converts microphone audio into text
import speech_recognition as sr
# Offline text-to-speech engine
import pyttsx3
# Language translation 
from googletrans import Translator

def speak(text, language='en'):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # 150 words per minute
    voices = engine.getProperty('voices')

    # Select voice
    if language == 'en':
        engine.setProperty('voice', voices[0].id)  # English voice
    else:
        engine.setProperty('voice', voices[1].id)  # Other language voice

    engine.say(text)
    engine.runAndWait()


def speech_to_text():
    recognizer = sr.Recognizer()
    
    # List available microphones
    print("Available microphones:")
    for i, name in enumerate(sr.Microphone.list_microphone_names()):
        print(f"{i}: {name}")
    

    # Use default mic (you can change device_index if needed)
    with sr.Microphone() as source:
        # Calibrate for ambient noise
        print("Calibrating microphone for ambient noise...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        
        print("Speak now in English:")
        try:
            audio = recognizer.listen(source)
        except sr.WaitTimeoutError:
            print("❌ No speech detected")
            return None

    try:
        text = recognizer.recognize_google(audio, language="en-US")
        print("✅ You said:", text)
        return text
    except sr.UnknownValueError:
        print("❌ Could not understand audio")
        return None
    except sr.RequestError as e:
        print("❌ Google API request failed:", e)
        return None


def translate_text(text, target_language='hi'):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    print("The translated text is:", translation.text)
    return translation.text


def display_language_options():
    print("Select target language:")
    print("1. Hindi")
    print("2. Tamil")
    print("3. Telugu")
    print("4. Bengali")
    print("5. Marathi")
    print("6. Gujarati")
    print("7. Malayalam")
    print("8. Punjabi")
    
    choice = input("Enter number (1–8): ").strip()
    languages = {
        "1": "hi", "2": "ta", "3": "te", "4": "bn",
        "5": "mr", "6": "gu", "7": "ml", "8": "pa"
    }
    return languages.get(choice, 'hi')


if __name__ == "__main__":
    target_lang = display_language_options()
    text = speech_to_text()
    
    if text:
        translated = translate_text(text, target_language=target_lang)
        speak(translated)
        print("🔊 Done!")
    else:
        print("⚠ No valid input detected. Exiting.")
