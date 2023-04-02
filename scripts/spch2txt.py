import pyaudio
import wave
import whisper


# Set audio parameters
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"

import os

# Set the path to the .wav file
file_path = "/scripts/" + WAVE_OUTPUT_FILENAME

# Check if the file exists
if os.path.exists(file_path):
    os.remove(file_path)

# Initialize PyAudio
audio = pyaudio.PyAudio()
model = whisper.load_model("base")

# Open microphone stream
stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)

print("we're recording!")
# Record audio from microphone
frames = []
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

# Stop recording
stream.stop_stream()
stream.close()
audio.terminate()

# Save audio as .wav file
wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(audio.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()

result = model.transcribe(WAVE_OUTPUT_FILENAME)["text"]
print(result)

import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()

# Set the voice properties
voices = engine.getProperty('voices')
voice_id = 1  # Change this number to use a different voice
engine.setProperty('voice', voices[voice_id].id)

# Convert text to speech
engine.say(result)
engine.runAndWait()


