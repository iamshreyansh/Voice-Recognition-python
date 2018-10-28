import csv
import sys
comp1=[];
comp2=[];
g=0
filename = "speccl"+".csv"
filename2 = "speccl2"+".csv"
f = open(filename, 'rt')
f2 = open(filename2, 'rt')
try:
    reader = csv.reader(f)
    for row in reader:
        comp1.append(float(row[1]));
	reader = csv.reader(f2)
    for row in reader:
        comp2.append(float(row[1]));
finally:
    f.close()
for i in range(583680):
	 if ((comp1[i]<comp2[i]+2) and  (comp1[i]>comp2[i]-2)):
	     g=g+1
	   
if g>58368:
  print 'Audio Match'
  h=float(float(float(g)/583680)*100)
  print h,'% match'
else:
 print 'Not a Match'