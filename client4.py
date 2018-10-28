import socket
import pyaudio
import wave
import pyaudio
import math
import time
import wave
import struct
import numpy.fft
import subprocess 
import pickle
import Tkinter
from threading import Thread
from time import gmtime, strftime
import tkFont
from Tkinter import *
from tkFileDialog import askopenfilename
from tkSimpleDialog import askstring
from tkMessageBox import *


#record
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 4
T="IP Address"
s="0"
st1="2"
user1="abc"
cafe="abc"
i=0

COLORframes = "#000080"                 # Color = "#rrggbb" rr=red gg=green bb=blue, Hexadecimal values 00 - ff
COLORcanvas = "#000000"
COLORgrid = "#808080"
COLORtrace1 = "#00ff00"
COLORtrace2 = "#ff8000"
COLORtext = "#ffffff"
COLORsignalband = "#ff0000"
COLORaudiobar = "#606060"
COLORaudiook = "#00ff00"
COLORaudiomax = "#ff0000"


# Button sizes that can be modified
Buttonwidth1 = 12
Buttonwidth2 = 8

  

def stri():
    global T
    global st
    st = askstring("IP Address",str(T))

def reglog():
    global st1
    st1= askstring("Registration/Login","1. Registration \n"+"2. Login\n")
 
def user():
    global user1
    user1= askstring("Username","Please fill in your username")

def grb():
    global data1


tk = Tkinter.Tk()
tk.withdraw()
#tk.minsize(200,200)
stri()


HOST = st                # The remote host
PORT = 50003             # The same port as used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))


reglog()
s.sendall(st1)
def reg():
    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

    print("*recording")

    frames = []
    
    for i in range(0, int(RATE/CHUNK*RECORD_SECONDS)):
        data  = stream.read(CHUNK)
        frames.append(data)
        s.sendall(data)

    print("*done recording")
    stream.stop_stream()
    stream.close()
    p.terminate()  
    
    print("*closed")
    
    s.close()
    i=i+1
	
	
def reg2():
    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

    print("*recording")

    frames = []
    
    for i in range(0, int(RATE/CHUNK*RECORD_SECONDS)):
        data  = stream.read(CHUNK)
        frames.append(data)
        s.sendall(data)

    print("*done recording")
    stream.stop_stream()
    stream.close()
    p.terminate()  
    
    print("*closed")
    
    s.close()
    i=i+1
    time.sleep(14)
    subprocess.call("g2.py", shell=True)
   
   


if st1=='1':
    user()
    s.sendall(user1)
    tk = Tkinter.Tk()
    ca = Canvas(tk,background='blue', width=200, height=200)
    ca.pack(expand=YES,fill=BOTH)
    b = Tkinter.Button(tk, text="Begin Recording Password",height=2,background='lightgreen', command=reg)
    b.pack(expand=YES,fill=BOTH)
    while True: 
                tk.update()
                if i==3:
                        break
    

   
if st1=='2':
    user()
    s.sendall(user1)
    tk = Tkinter.Tk()
    ca = Canvas(tk,background='lightblue', width=200, height=200)
    ca.pack(expand=YES,fill=BOTH)
    b = Tkinter.Button(tk, text="Begin Recording Password",height=2,background='lightgreen',command=reg2)
    b.pack(expand=YES,fill=BOTH)
    while True: 
        tk.update()
        if i==3:
            break

 

