# Speech to Text


## Design

The overall design consists of a multithreading system that uses Google's Speech to Text API. 

One thread adds the audio files to the thread-safe queue and two consumer threads execute the audio transcription synchronously. Currently supports MP3 audio files of 1 minute of length and 44000 Hz sample rate. All queued items have same priority. 

Next steps:
- In order to find the number of API calls to run simultaneously, I will perform a CPU analysis to find the bottleneck of the system when calling all APIs.

### Files
- speech-to-text.py: Multi-threaded audio transcription
- threader.py: Multi-threading exercise
- processes.py: Multi-processing exercise

### References
- [Getting Started with Google Cloud Speech-To-Text API in Python](https://www.youtube.com/watch?v=lKra6E_tp5U)
- [Google Cloud Speech-to-Text](https://cloud.google.com/speech-to-text/docs/sync-recognize)
- [Sample MP3 audio files](movie-sounds.org)