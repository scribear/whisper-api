from flask import Flask, request, jsonify
import soundfile as sf
import io
import transcriber
from pydub import AudioSegment
import numpy as np
import os
import uuid

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route('/transcribe', methods=['POST'])
def transcribe():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file:
        # Generate a unique filename to avoid collisions
        unique_filename = str(uuid.uuid4()) + os.path.splitext(file.filename)[1]
        filepath = os.path.join(UPLOAD_FOLDER, unique_filename)
        
        # Save the file
        file.save(filepath)
        
        # Pass the file path to the transcriber
        transcription = transcriber.transcribe(filepath)
        
        # Optionally, delete the file after transcription
        # os.remove(filepath)
        
        # Call the internal transcribe function
        transcription = transcriber.transcribe(filepath)
        
        return jsonify({'transcription': transcription})
    else:
        return jsonify({'error': 'Invalid file format'}), 400

@app.route('/multilingual', methods=['POST'])
def recognize_multilingual():
    # Implement your code here to handle the audio transcription for multilingual content
    # You can access the audio file and other parameters from request.files and request.form
    return jsonify({'transcription': 'Transcribed text goes here'})

if __name__ == '__main__':
    app.run(port=5000, debug=True)