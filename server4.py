# Echo server program
import socket
import pyaudio
import wave
import time
import subprocess
import sys


CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 4
WAVE_OUTPUT_FILENAME = "server_output1.wav"
WIDTH = 2
frames = []
j=1


p = pyaudio.PyAudio()
stream = p.open(format=p.get_format_from_width(WIDTH),
                channels=CHANNELS,
                rate=RATE,
                output=True,
                frames_per_buffer=CHUNK)


HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50003              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print 'Connected by', addr
st1=conn.recv(1024)
print st1
user1=conn.recv(1024)
print user1
filename = "use" 
filename = filename + ".txt"

Wfile = open(filename,'w')                        # Open output file
Wfile.write(user1)              
Wfile.close()      
if st1=='1':
 data = conn.recv(1024)
 i=1
 while data != '':
     stream.write(data)
     data = conn.recv(1024)
     i=i+1
     #print i
     frames.append(data)


 wf = wave.open(user1+".wav", 'wb')
 wf.setnchannels(CHANNELS)
 wf.setsampwidth(p.get_sample_size(FORMAT))
 wf.setframerate(RATE)
 wf.writeframes(b''.join(frames))
 wf.close()
 stream.stop_stream()
 stream.close()
 p.terminate()
 subprocess.call("speechrec3.py", shell=True)
 conn.close()

 
 
elif st1=='2':
 data = conn.recv(1024)
 i=1

 while data != '':
     stream.write(data)
     data = conn.recv(1024)
     i=i+1
     #print i
     frames.append(data)
 wf = wave.open(user1+"1.wav", 'wb')
 wf.setnchannels(CHANNELS)
 wf.setsampwidth(p.get_sample_size(FORMAT))
 wf.setframerate(RATE)
 wf.writeframes(b''.join(frames))
 wf.close()
 stream.stop_stream()
 stream.close()
 p.terminate()
 conn.close()

 subprocess.call("speechrec4.py", shell=True)
