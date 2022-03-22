# Example from 'Getting Started with Google Cloud Speech-To-Text API in Python' by Jie Jenn

import os
from google.cloud import speech
import threading, queue

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'health-app-2022-75164cf9a820.json'
audio_list = ['never-give-up-and-good-luck-will-find-you.mp3' ]

q = queue.Queue()

def transcription():
# Step 1. 
    speech_client = speech.SpeechClient()
    # audio_mp3 = 'never-give-up-and-good-luck-will-find-you.mp3'   # file is 6s long
    
    audio_mp3 = q.get()

# def load_files():
    # Step 2. Create speech recongition instance (synchronous recognition)
    with open(audio_mp3, 'rb') as f1:
        byte_data_mp3 = f1.read()
    audio_recognition = speech.RecognitionAudio(content=byte_data_mp3)


# def configure():
    # Step 3. Configurations for audio file
    config_mp3 = speech.RecognitionConfig(
        sample_rate_hertz=44000,
        language_code="en-US",
        enable_automatic_punctuation=True
    )


# def transcribe(config, audio_recognition):
    # Step 4. Transcribe audio file (MP3)
    response = speech_client.recognize(
        config=config_mp3,
        audio=audio_recognition
    )

    for result in response.results:
        print(u"Transcript: {}".format(threading.current_thread().name, result.alternatives[0].transcript))


def add_files():
    for file in audio_list:
        q.put(file)
    
        print(f'{threading.current_thread().name} adding {file}')


threading.Thread(target=transcription, daemon=True).start()
threading.Thread(target=add_files, daemon=True).start()


q.join()
print('All work completed')
