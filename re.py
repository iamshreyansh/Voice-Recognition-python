import subprocess
import time

g=0
m=0
for i in range(1,46):
	j=str(i)
	print "Doctor "+j
	for k in range(12,0,-1):
		if k<10:
			l=str(k)
			file = open(j+'.txt', 'r')
			line = file.readline()
			line2=line[:1]
			if line2==l:
				g=g+1
			while line:
				line = file.readline()
				line2=line[:1]
				if line2==l:
					g=g+1
		else:
			l=str(k)
			file = open(j+'.txt', 'r')
			line = file.readline()
			line2=line[:2]
			if line2==l:
				g=g+1
				m=m+1
			while line:
				line = file.readline()
				line2=line[:2]
				if line2==l:
					g=g+1
					m=m+1
		if k==1:
			g=g-m;
		file.close()
		h=str(g)
		
		print "number of"+l+":"+h
		g=0
	print "\n\n"
	m=0