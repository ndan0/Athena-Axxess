import pyaudio
import wave
import whisper

def speech2text():
    WAVE_OUTPUT_FILENAME = "output.wav"
    model = whisper.load_model("base")
    result = model.transcribe(WAVE_OUTPUT_FILENAME)["text"]
    return result
    # import pyttsx3

    # # Initialize the TTS engine
    # engine = pyttsx3.init()

    # # Set the voice properties
    # voices = engine.getProperty('voices')
    # voice_id = 1  # Change this number to use a different voice
    # engine.setProperty('voice', voices[voice_id].id)

    # # Convert text to speech
    # engine.say(result)
    # engine.runAndWait()


