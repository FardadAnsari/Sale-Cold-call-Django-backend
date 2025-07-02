import whisper
import numpy as np
import sounddevice as sd
import torch
import queue
import os

class CallTranscriptionManager:
    def __init__(self, agent_id):
        self.agent_id = agent_id
        self.q = queue.Queue()
        self.running = True

    def callback(self, indata, frames, time, status):
        if status:
            print(f"[Status] {status}", flush=True)
        self.q.put(indata.copy())  # indata is already a numpy array

    def run_live_transcription(self):
        model = whisper.load_model("base")
        samplerate = 16000
        block_duration = 5  # seconds
        blocksize = int(samplerate * block_duration)

        os.makedirs("transcripts", exist_ok=True)
        transcript_path = f"transcripts/{self.agent_id}.txt"

        with sd.InputStream(samplerate=samplerate,
                            channels=1,
                            dtype='float32',
                            blocksize=blocksize,
                            callback=self.callback):
            print(f"🎙️ Listening for agent: {self.agent_id} (Press Ctrl+C to stop)")
            with open(transcript_path, "w", encoding="utf-8") as f:
                while self.running:
                    try:
                        audio_chunk = self.q.get()
                        audio_data = audio_chunk.flatten()
                        audio_data = whisper.pad_or_trim(audio_data)
                        mel = whisper.log_mel_spectrogram(audio_data).to(model.device)

                        options = whisper.DecodingOptions(language="en", fp16=torch.cuda.is_available())
                        result = whisper.decode(model, mel, options)

                        text = result.text.strip()
                        if text:
                            print("🗣️", text)
                            f.write(text + "\n")
                    except Exception as e:
                        print(f"[ERROR] {e}", flush=True)
