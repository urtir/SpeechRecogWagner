import os
import queue
import sounddevice as sd
import vosk
import json

# Inisialisasi model Vosk (pastikan path sesuai dengan lokasi model)
model_path = "C:/Users/risqu/Desktop/SPEECH RECOG OFFLINE/vosk-model-small-en-us-0.15"  # Sesuaikan path dengan lokasi model Anda
if not os.path.exists(model_path):
    print("Model tidak ditemukan. Unduh model dari https://alphacephei.com/vosk/models dan ekstrak ke path yang sesuai.")
    exit(1)

model = vosk.Model(model_path)
recognizer = vosk.KaldiRecognizer(model, 16000)

# Buat queue untuk menangkap audio
q = queue.Queue()

# Callback function untuk menangkap audio
def callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))

# Mulai streaming audio
with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                       channels=1, callback=callback):
    print("Microphone standby... please talk.")

    while True:
        data = q.get()
        if recognizer.AcceptWaveform(data):
            result = json.loads(recognizer.Result())
            text = result['text']
            print(f"Text: {text}")

            if "please stop all of this" in text.lower():
                print("finishing talk, exiting")
                break  # Menghentikan loop
        else:
            partial_result = json.loads(recognizer.PartialResult())
            print(f"Partial result: {partial_result['partial']}")

print("program finished")
