# SPEECH-RECOGNITION-SYSTEM

COMPANY CODTECH IT SOLUTIONS

NAME: KONDA KRISHNAVENI

INTERN ID: ID:CODF46

ARTIFICIAL INTELLIGENCE MARKUP LANGUAGE

DURATION: 4 WEEEKS

MENTOR: NEELA SANTOSH

As part of the CodTech AIML Internship, Task 2 focuses on building a Speech Recognition System using Python. The aim of this project is to convert spoken audio into written text by leveraging machine learning techniques and publicly available speech recognition tools. This project is a great example of how artificial intelligence can be applied to solve real-world problems such as transcription, voice control, and accessibility for differently-abled users.

The project starts by allowing the user to upload an audio file, usually in .wav format. The system processes the uploaded audio using the speech_recognition library — a powerful and beginner-friendly Python package that supports multiple backends, including Google Web Speech API. The uploaded audio is read and passed to the recognizer which listens to the content and attempts to convert the speech into human-readable text.

Several tasks were performed to make this speech recognition system functional. The first task was to install and import necessary libraries such as speech_recognition, and, optionally, pydub for file conversion. Using Google Colab as the development environment helped bypass local setup challenges and allowed file uploads and processing in the cloud with minimal effort. Once the file was uploaded, the program used the recognizer object from the speech_recognition module to process the audio. The recognize_google() method was used to send the audio to Google’s speech recognition service, which returned the transcribed text if successful.

In this project, error handling was an important part of the process. If the speech was unclear or the API failed to respond, the code handled these exceptions gracefully by printing appropriate messages. This ensured that the system was robust and could handle real-world variations in audio quality or network interruptions.

The entire code was written and executed in Google Colab, a popular cloud-based Python editor. Google Colab is especially convenient because it supports uploading files, installing libraries, and running code without any need for local software setup. It also works well on mobile devices, which was helpful during this internship. After successful development and testing, the Python script was downloaded in .py format and uploaded to GitHub for version control and submission.


This project has several real-world applications. It can be used in voice assistants (like Siri, Alexa, Google Assistant), transcription services (for interviews, lectures, meetings), assistive technologies for users with disabilities (like hands-free writing), and in smart home or IoT devices for voice control. As speech interfaces become more common, the ability to build simple but effective speech recognition tools is a valuable skill for any AI/ML developer.

In summary, Task 2 provided a hands-on opportunity to apply machine learning and NLP concepts to create a speech-based application. It helped build familiarity with speech-to-text technologies and cloud-based development environments. The project is simple, yet powerful, and lays the groundwork for more advanced voice-interactive systems. Completing this task strengthened both my coding skills and my understanding of how AI can be used to solve real-world problems through automation and accessibility.

OUTPUT :

![Image](https://github.com/user-attachments/assets/24303a4a-c4bc-4c13-b6d1-b11fcb481d3b)
