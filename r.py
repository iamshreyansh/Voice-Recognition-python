import subprocess

g=0
file = open('use.txt', 'r')
u=file.read()
filename2 = u+"1"+".txt"

f2 = open(filename2, 'rt')

first2=f2.readline()

print first2+"cdf"
