# Example from 'Getting Started with Google Cloud Speech-To-Text API in Python' by Jie Jenn

import os
from google.cloud import speech

# Step 1. 
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'health-app-2022-75164cf9a820.json'
speech_client = speech.SpeechClient()
audio_mp3 = 'never-give-up-and-good-luck-will-find-you.mp3'   # file is 6s long

# Step 2. Create speech recongition instance
with open(audio_mp3, 'rb') as f1:
	byte_data_mp3 = f1.read()
audio_recongition = speech.RecognitionAudio(content=byte_data_mp3)

# Step 3. Configurations for audio file
config_mp3 = speech.RecognitionConfig(
    sample_rate_hertz=44000,
    language_code="en-US",
    enable_automatic_punctuation=True
)

# Step 4. Transcribe audio file (MP3)
respondoutput = speech_client.recognize(
	config=config_mp3,
	audio=audio_recongition
)

print(respondoutput)