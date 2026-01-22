from deep_translator import GoogleTranslator
import os

# ===================== LANGUAGE VOICE MAPPING =====================
language_voice_map = {
    "hi": "Lekha",    # Hindi
    "ta": "Veena",    # Tamil
    "te": "Lekha",    # Telugu (reuse Hindi voice)
    "bn": "Lekha",    # Bengali (reuse Hindi voice)
    "mr": "Lekha",    # Marathi (reuse Hindi voice)
    "gu": "Lekha",    # Gujarati (reuse Hindi voice)
    "ml": "Lekha",    # Malayalam (reuse Hindi voice)
    "pa": "Lekha",    # Punjabi (reuse Hindi voice)
    "en": "Alex",     # English
    "de": "Anna",     # German
    "el": "Yelda",    # Greek (example, pick an installed Greek voice)
    "es": "Jorge"     # Spanish (example, pick an installed Spanish voice)
}

# ===================== LANGUAGE SELECTION =====================
def select_language():
    print("Available translation languages are: ")
    print("1. Hindi (hi)")
    print("2. Spanish (es)")
    print("3. Bengali (bn)")
    print("4. German (de)")
    choice = input("Select the language number 1-4: ")
    language_dict = {"1": "hi", "2": "es", "3": "bn", "4": "de"}
    selection = language_dict.get(choice, "hi")
    return selection

# ===================== TRANSLATION =====================
def translate_text(original_text, target_language):
    try:
        translated_text = GoogleTranslator(source="en", target=target_language).translate(original_text)
        print("🌍 Translated text:", translated_text)
        return translated_text
    except Exception as e:
        print("❌ Translation failed:", e)
        return original_text

# ===================== SPEECH =====================
def speak(text, lang_code="en"):
    """
    Speak text using macOS 'say' command with language-appropriate voice.
    """
    voice_name = language_voice_map.get(lang_code, "Alex")  # fallback to English
    try:
        os.system(f'say -v "{voice_name}" "{text}"')
    except Exception as e:
        print("❌ Speech synthesis failed:", e)

# ===================== MAIN =====================
if __name__ == "__main__":
    target_language = select_language()
    original_text = input("Please enter the text to be translated here: ")
    translated_text = translate_text(original_text, target_language)
    speak(translated_text, lang_code=target_language)
