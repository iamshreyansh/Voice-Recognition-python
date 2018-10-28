import speech_recognition as sr
r = sr.Recognizer()
r.energy_threshold = 4000
with sr.Microphone() as source:                # use the default microphone as the audio source
    print "You said"
    audio = r.listen(source)                   # listen for the first phrase and extract it into audio data


try:
    print(r.recognize(audio))    # recognize speech 
except LookupError:                            # speech is unintelligible
    print("Could not understand audio")
