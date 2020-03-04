#Build a FTP script to delete spool files from list of spool files.
#RUN AS FOLLOWS:
#python cleanspl.py x YES qprtsplq.txt cleanspl.cmd.ftp
#quote rcmd dltsplf file(XXX) JOB(number/username/jobname)
import sys
import re
import string
import datetime
import os
import csv
ddebug=sys.argv[2]
fileI1=sys.argv[3]
fileO1=sys.argv[4]
dirlim=chr(92)#\
bslsh=chr(47) #/
quotes=chr(34)#"
parl=chr(40)
parr=chr(41)
x=0
if ddebug == "YES":
	print("Let's read input from a TXT file ! ! ! ! ")

fi1 = open(fileI1)
fo1 = open(fileO1, 'w')
spoolfile=""
jobuser=""
jobnumber=""
jobname=""
spoolnum=""
rline = fi1.readline()
while rline:
	spoolfile = rline[0:12].strip()
	if ddebug == "YES":
		print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
		#print(rline)
		print(rline[:8])
		print("SPOOLFILE:" + quotes + spoolfile + quotes)
	if spoolfile == "5770SS1 V7R":
		if ddebug == "YES":
			print ("Found Serial Number: " + spoolfile)
			print("SPOOLFILE:" + quotes + spoolfile + quotes)
		rline = fi1.readline()
		spoolfile = rline[0:12].strip()
		x=x+1
	if spoolfile == "File":
		if ddebug == "YES":
			print ("Found Page Label: "+ spoolfile)
			print("SPOOLFILE:" + quotes + spoolfile + quotes)
		rline = fi1.readline()
		spoolfile = rline[0:12].strip()
		x=x+1
	if spoolfile == "":
		if ddebug == "YES":
			print ("Found blank line: "+ spoolfile)
			print("SPOOLFILE:" + quotes + spoolfile + quotes)
		rline = fi1.readline()
		spoolfile = rline[0:12].strip()
		x=x+1
	spoolfile = rline[0:12].strip()
	jobname = rline[83:94].strip()
	jobuser = rline[12:23].strip()
	jobnumber = rline[94:101].strip()
	spoolnum = rline[73:83].strip()
	clnspl = "DLTSPLF FILE" + parl + spoolfile + parr + " JOB" + parl + jobnumber + bslsh + jobuser + bslsh + jobname + parr + " SPLNBR" + parl + spoolnum + parr
	if ddebug == "YES":
		#print("DLTSPLF FILE" + parl + spoolfile + parr + "JOB" + parl + jobnumber + bslsh + jobuser + bslsh + jobname + parr)
		print(clnspl)
	fo1.write("quote rcmd " + clnspl + "\n")
	
	x=x+1
	rline = fi1.readline()
print("lines read: " + str(x-1))