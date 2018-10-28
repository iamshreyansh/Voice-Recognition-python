import speech_recognition as sr
r = sr.Recognizer()
with sr.WavFile("ayush14.wav") as source:              # use "ayush10.wav" as the audio source
    audio = r.record(source)                        # extract audio data from the file

try:
    print("Transcription: " + r.recognize(audio))   # recognize speech 
except LookupError:                                 # speech is unintelligible
    print("Could not understand audio")
