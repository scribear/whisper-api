import whisper
import numpy as np

def transcribe(filepath):
    '''Returns a string with the transcription'''
    model = whisper.load_model("base")

    # TODO preprocessing?
    # audio_data = audio_data.astype(np.float32)

    # Perform transcription using the Whisper model
    result = model.transcribe(filepath)

    return result['text']