import subprocess
import time
time.sleep(3)

g=0
file = open('use.txt', 'r')
u=file.read()
filename = u+".txt"
filename2 = u+"1"+".txt"
f = open(filename, 'r')
f2 = open(filename2, 'r')
first1=f.readline()
first2=f2.readline()
if first1==first2:
 g=1
 print g
if g==1:
 subprocess.call("spec11.py", shell=True) 
