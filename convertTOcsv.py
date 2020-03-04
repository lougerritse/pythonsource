#Build a FTP script to convert a spool file from work out queue to csv for upload into db.
#RUN AS FOLLOWS:
#python convertTOcsv.py x YES [INPUT FILE] [OUTPUT CSV FILE]
#python convertTOcsv.py x YES qprtsplq.txt cleanspl.cmd.ftp
#FORMAT MUST MATCH...
#IF OS Release changes this code may need to change!!
#HEADER ROW:
# File       User       User Data  Status Pages Copies Form Type  Pty File Number   Job        Number Date     Time
#"FILE,USER,USERDATA,SATUS,PAGES,COPIES,FORMTYPE,PTY,FILENUMBER,JOB,JOBNUMBER,DATE,TIME"

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
hr=0
hc=0
x=0
z=0
if ddebug == "YES":
	print("Let's read input from a TXT file ! ! ! ! ")
c01=""
c02=""
c03=""
c04=""
c05=""
c06=""
c07=""
c08=""
c09=""
c10=""
c11=""
c12=""
c13 =""
fi1 = open(fileI1)
fo1 = open(fileO1, 'w')
search1="Work With Output Queue"
search2="File       User       User Data  Status"
rline = fi1.readline()
#write the header to the output file.
fo1.write("FILE,USER,USERDATA,SATUS,PAGES,COPIES,FORMTYPE,PTY,FILENUMBER,JOB,JOBNUMBER,DATE,TIME\n")
while rline:
	if ddebug == "YES":
		print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
		#print(rline)
		print(rline[:8])
	s1 = re.search(search1, rline)
	if s1:
		rline = fi1.readline()
		if ddebug == "YES":
			hr=hr+1
			print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
			print("FOUND A REPORT HEADER ! - - - - - - - - - - - - - - - - - - - - - - -")
			print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
	s2 = re.search(search2, rline)
	if s2:
		rline = fi1.readline()
		if ddebug == "YES":
			hc=hc+1
			print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
			print("FOUND A COLUMN HEADER ! - - - - - - - - - - - - - - - - - - - - - - -")
			print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
			#print("DLTSPLF FILE" + parl + spoolfile + parr + "JOB" + parl + jobnumber + bslsh + jobuser + bslsh + jobname + parr)
		#print(clnspl)
	c01=(rline[0:11].strip())
	c02=(rline[12:22].strip())
	c03=(rline[23:34].strip())
	c04=(rline[35:40].strip())
	c05=(rline[41:46].strip())
	c06=(rline[47:53].strip())
	c07=(rline[54:64].strip())
	c08=(rline[65:72].strip())
	c09=(rline[73:82].strip())
	c10=(rline[82:93].strip())
	c11=(rline[94:100].strip())
	c12=(rline[101:109].strip())
	c13=(rline[110:118].strip())
	rptline=c01 + "," + c02 + "," + c03 + "," + c04 + "," + c05 + "," + c06 + "," + c07 + "," + c08 + "," + c09 + "," + c10 + "," + c11 + "," + c12 + "," + c13 + "\n"
	fo1.write(rptline)
	#fo1.write(rline)
	if ddebug == "XXX":
		z=z+1
		fo1.write(rline)
		if z>1000:
			break
	if ddebug == "YES":
		print(rptline)
	x=x+1
	rline = fi1.readline()
print("- - - - - Lines read: " + str(x-1))
if ddebug == "YES":
	print("Report Headers Found: " + str(hr))
	print("Column Headers Found: " + str(hc))