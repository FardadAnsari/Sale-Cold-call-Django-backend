import whisper
import sounddevice as sd
import numpy as np
import torch
import queue

# Load Whisper model
model = whisper.load_model("small")

def record_audio(duration=5, fs=16000):
    try:
        print(f"[INFO] Recording for {duration} seconds...")
        audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype="float32")
        sd.wait()
        return np.squeeze(audio)
    except Exception as e:
        print(f"[ERROR] Audio recording failed: {e}")
        return None

def transcribe(audio_data):
    try:
        audio_data = whisper.pad_or_trim(audio_data)
        mel = whisper.log_mel_spectrogram(audio_data).to(model.device)
        options = whisper.DecodingOptions(language="en", fp16=torch.cuda.is_available())
        result = whisper.decode(model, mel, options)
        return result.text
    except Exception as e:
        print(f"[ERROR] Transcription failed: {e}")
        return ""

# Main loop
print("[INFO] Live transcription started. Press Ctrl+C to stop.")
try:
    while True:
        audio = record_audio(duration=5)
        if audio is not None:
            text = transcribe(audio)
            if text.strip():
                print("🗣️ You said:", text)
            else:
                print("⚠️ No speech detected.")
except KeyboardInterrupt:
    print("\n[INFO] Transcription stopped.")