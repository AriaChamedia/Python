import threading #Allows multiple tasks to run simultaneously (recording + spinner + key press).
import sys #Used for writing output (sys.stdout.write) without new lines.
import time 
import sounddevice as sd #Captures live microphone audio.
import numpy as np #Converts raw audio bytes into numeric arrays.
import matplotlib.pyplot as plt #Used to plot the audio waveform.
from scipy.io.wavfile import write
import speech_recognition as sr
from speech_recognition import AudioData #Wraps raw audio bytes into a format recognizers can use.
# ---------------- GLOBAL STOP FLAG ----------------
stop_event = threading.Event()


def wait_for_enter():
    input("Press Enter to stop recording")
    stop_event.set()
    
# ---------------- SPINNER ----------------
def spinner():
    chars = "|/-\\"
    i = 0
    while not stop_event.is_set():
        sys.stdout.write(f"\r🔴 Recording... {chars[i % 4]}")
        sys.stdout.flush()
        i += 1
        time.sleep(0.1)
    print("\r✅ Recording complete!        ")



# ---------------- RECORD AUDIO ----------------
def record_audio():
    rate = 16000
    frames = []
    #callback: A function that is called with new audio data if using the non-blocking method. 
    def callback(indata, frames_count, time_info, status):
        frames.append(indata.copy())

    stream = sd.InputStream(
        samplerate=rate,
        channels=1,
        dtype="int16",
        callback=callback
    )

    threading.Thread(target=wait_for_enter, daemon=True).start()
    threading.Thread(target=spinner, daemon=True).start()

    with stream:
        while not stop_event.is_set():
            time.sleep(0.1)

    audio_data = np.concatenate(frames, axis=0)
    return audio_data, rate

def save_audio(audio_data, rate,filename="recording.wav" ):
    write(filename, rate, audio_data) 
    print(f"💾 Saved: {filename}")
    
def main():
    print("Hello AI can you hear me?")
    print("Speak into your microphone")
    audio_data, rate = record_audio()
    save_audio(audio_data, rate)
    
    plot_waveform(audio_data, rate)

def plot_waveform(audio_data, rate):
    plt.figure(figsize=(10, 4))
    plt.plot(np.linspace(0, len(audio_data) / rate, num=len(audio_data)), audio_data)
    plt.title("Audio Waveform")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()