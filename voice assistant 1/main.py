import pyttsx3 
import speech_recognition as sr
import datetime 

engine = pyttsx3.init()
#rate = speech rate (speed of speaking) for pyttsx3.
engine.setProperty('rate', 150)
recognizer = sr.Recognizer()
def speak(text):
    engine.say(text)
    engine.runAndWait()
    
def get_audio():

    with sr.Microphone() as source:
        print("🎤 Speak now...")
        recognizer.adjust_for_ambient_noise(source, duration=0.7)
        
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            command = recognizer.recognize_google(audio)
            print(f"✅ You said: {command}")
            return command.lower()
        
        except sr.WaitTimeoutError:
            print("⌛ Listening timed out")
        except sr.UnknownValueError:
            print("❌ Could not understand")
        except sr.RequestError:
            print("Sorry, my internet connection is not working.")
        except sr.RequestError as e:
            print(f"❌ API Error: {e}")

    return "" 

def respond_to_command(command):
    if "hello" in command:
        speak("Hi there! How can I help you today?")
        
    elif "your name" in command:
        speak("I am your Python voice assistant.")
    elif "time" in command:
        now = datetime.now().strftime("%I:%M %p")
        speak(f"The time is {now}")
        
    elif "exit" in command or "stop" in command:
        speak("Goodbye!")
        return False
        
    else:
        speak("I'm not sure how to help with that.")

    return True
        
if __name__ == "__main__":
    speak("Voice assistant activated. Say something!")
    while True:
        command=get_audio()
        if command:
            respond_to_command(command)
            
    
    