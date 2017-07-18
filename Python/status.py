#!/usr/bin/python

print "Content-type:text/html\r\n\r\n"

import cgi, cgitb

form=cgi.FieldStorage()
username=form.getvalue('username')
update=form.getvalue('update')

if not update:
        print
else:
	with open("./orstatus.txt", "a") as appendFile:
		appendFile.write("%s wrote: %s\r\n"%(username, update))

#--reverse the order of the file to be in decreasing order
with open("./orstatus.txt") as f:
       with open("./revstatus.txt", "w") as fout:
               fout.writelines(reversed(f.readlines()))

#--store list of friends and username in a list
friends_list=[]
with open("/home/2016/jchen169/public_html/userFriends.txt","r") as friends_file:
	for line in friends_file:
		if line.split(' ', 1)[0]==username:
			for token in line.split( ):
				friends_list.append(token)

#--if first word in list, add to status.txt
with open("./revstatus.txt") as f2:
	with open("./status.txt", "w") as fout2:
		for status_line in f2:
			if status_line.split( )[0] == username:
				fout2.writelines(status_line)
         		elif status_line.split( )[0] in friends_list:
                                fout2.writelines(status_line)

#--check for only the first 20 line of statuses
with open("./status.txt", "r+") as myfile2:
       for I in range(0, 21):
               line=myfile2.readline()
       myfile2.truncate()

