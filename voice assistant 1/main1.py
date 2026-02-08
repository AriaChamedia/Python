import time
import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()
recognizer.dynamic_energy_threshold = True

engine = pyttsx3.init()
#rate = speech rate (speed of speaking) for pyttsx3.
engine.setProperty('rate', 150)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def get_audio():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.7)
        print("🎤 Speak now...")
        time.sleep(0.3)

        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=4)
            text = recognizer.recognize_google(audio)
            print("✅ You said:", text)
            return text.lower()

        except sr.WaitTimeoutError:
            print("⌛ No speech detected")
        except sr.UnknownValueError:
            print("❌ Could not understand")
        except sr.RequestError:
            print("❌ Internet/API issue")

    return ""

def respond_to_command(command):
    if "hello" in command:
        speak("Hi there! How can I help you today?")
        
    elif "your name" in command:
        speak("I am your Python voice assistant.")

        
if __name__ == "__main__":
    speak("Voice assistant activated. Say something!")
    while True:
        command=get_audio()
        if command:
            respond_to_command(command)
            