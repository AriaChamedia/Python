import sounddevice as sd
import numpy as np
import matplotlib.pyplot as plt
import speech_recognition as sr

SAMPLE_RATE = 16000

def record_audio(seconds, label):
    print(f"\n🎤 {label}")
    print(f"Recording for {seconds} seconds...")
    audio = sd.rec(int(seconds * SAMPLE_RATE),
                    samplerate=SAMPLE_RATE,
                    channels=1,
                    dtype='int16')
    sd.wait()
    print("✅ Recording finished")
    return audio.flatten()

def analyze_audio(samples):
    return {
        "duration": len(samples) / SAMPLE_RATE,
        "avg_volume": np.mean(np.abs(samples)),
        "max_volume": np.max(np.abs(samples)),
        "samples": samples
    }

def transcribe(samples):
    recognizer = sr.Recognizer()
    audio_data = sr.AudioData(samples.tobytes(), SAMPLE_RATE, 2)
    try:
        return recognizer.recognize_google(audio_data)
    except:
        return "[Could not transcribe]"

def display(stats, text, label):
    print("\n" + "-" * 30)
    print(f"📊 {label}")
    print("-" * 30)
    print(f"⏱ Duration: {stats['duration']:.2f} sec")
    print(f"🔊 Avg Volume: {stats['avg_volume']:.0f}")
    print(f"📈 Max Volume: {stats['max_volume']:.0f}")
    print(f"📝 Text: {text}")

def compare(s1, s2):
    print("\n🔬 COMPARISON")
    louder = "1" if s1['avg_volume'] > s2['avg_volume'] else "2"
    longer = "1" if s1['duration'] > s2['duration'] else "2"
    print(f"Recording {louder} is louder")
    print(f"Recording {longer} is longer")

def plot_audio(s1, s2):
    plt.figure(figsize=(10,5))
    plt.subplot(2,1,1)
    plt.plot(s1['samples'])
    plt.title("Recording 1")
    plt.subplot(2,1,2)
    plt.plot(s2['samples'])
    plt.title("Recording 2")
    plt.tight_layout()
    plt.show()

def main():
    print("🔬 VOICE ANALYSIS LAB (Updated)")

    samples1 = record_audio(4, "Recording 1: Speak normally")
    stats1 = analyze_audio(samples1)
    text1 = transcribe(samples1)
    display(stats1, text1, "Recording 1")

    input("\nPress Enter to record again...")
    samples2 = record_audio(4, "Recording 2: Speak louder/faster")
    stats2 = analyze_audio(samples2)
    text2 = transcribe(samples2)
    display(stats2, text2, "Recording 2")

    compare(stats1, stats2)
    plot_audio(stats1, stats2)

if __name__ == "__main__":
    main()
