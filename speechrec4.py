import subprocess
import speech_recognition as sr
import time
r = sr.Recognizer()

file = open('use.txt', 'r')
u=file.read()
filename=u+"1.wav"
file2=open(u+"1.txt",'w')
with sr.WavFile(filename) as source:              # use "ayush8.wav" as the audio source
    audio = r.record(source)                        # extract audio data from the file

try:
    list = r.recognize(audio,True)                  # generate a list of possible transcriptions
    print("Possible transcriptions:")
    for prediction in list:
        print(" " + prediction["text"] + " (" + str(prediction["confidence"]*100) + "%)")
	file2.write( prediction["text"]+"\n" )
  
    
		
except LookupError:                                 # speech is unintelligible
    print("Could not understand audio")	
file2.close()
file2=open(u+"1.txt",'r')
file2.close()
subprocess.call("read2.py", shell=True)

