import json
import pyaudio

from vosk import Model, KaldiRecognizer

model = Model('/run/media/yaroslav/D/IT_work/goiteens/python_1y_15_22/lessons/semester II/lesson3/vosk-model-en-us-0.22-lgraph')
recongizer = KaldiRecognizer(model, 16000)
words = pyaudio.PyAudio()
stream = words.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)

stream.start_stream()

def listen():
    while True:
        data =stream.read(4000, exception_on_overflow=False)
        if (recongizer.AcceptWaveform(data)) and len(data) > 0:
            answer = json.loads(recongizer.Result())
            if answer['text']:
                yield answer['text']


for text in listen():
    print(f'User: {text}')