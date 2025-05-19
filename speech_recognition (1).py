# Install the speech recognition library
!pip install SpeechRecognition

# Import the library and upload the audio file
import speech_recognition as sr
from google.colab import files
uploaded = files.upload()

"""# New Section"""

# Prepare the recognizer and load the audio file
audio_file = next(iter(uploaded))  # Get the uploaded file name
recognizer = sr.Recognizer()

with sr.AudioFile(audio_file) as source:
    audio_data = recognizer.record(source)  # Load the full audio

# Convert the audio to text
try:
    text = recognizer.recognize_google(audio_data)
    print("Transcribed Text:")
    print(text)
except sr.UnknownValueError:
    print("Sorry, could not understand the audio.")
except sr.RequestError as e:
    print(f"Could not request results; {e}")

# Display the final result
print("Final Transcription:")
print(text)

