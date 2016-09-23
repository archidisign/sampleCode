#!/usr/bin/python
import cgi, cgitb

form=cgi.FieldStorage()
username=form.getvalue('username')
friendName=form.getvalue('friendName')

fullName="sample"
jobDescription="sample2"

print "Content-type:text/html\r\n\r\n"
print "<HTML>"
print "<HEAD>"
print "<STYLE>"
print "MARK{"
print "        background-color: white;"
print "        color:black;"
print "}"

print "input[type=submit] {"
print "         background-color: #000000;"
print "         border: none;"
print "         color: white;"
print "         padding: 14px 20 px;"
print "         text-decoration: none;"
print "         margin: 4px 2px;"
print "         cursor: pointer;"
print "}"
print "a{"
print "         background-color: #000000;"
print "         border: none;"
print "         color: white;"
print "         padding: 14px 20 px;"
print "         text-decoration: none;"
print "         margin: 4px 2px;"
print "         cursor: pointer;"
print "}"

print "</style>"
print "<title>%s</title>"%(friendName)
print "</head>"

print "<body background=\"http://cgi.cs.mcgill.ca/~dzhang52/background_Pattern.jpg\">"

print "<center><h1><mark>%s's Profile Page</mark> </h1></center>"%(friendName)
print "<center><p><mark>Dear friend, welcome to my profile page!</mark></p></center>"

print "<br><br>"

print "<center><h3><mark>Username: %s</mark> </h3></center>"%(friendName)

open_file=open("/home/2016/lcolom2/public_html/cgi-bin/user",'r')
f=open_file.readlines()
with open("/home/2016/lcolom2/public_html/cgi-bin/user", 'r') as myfile:
	lines_list=myfile.readlines()
num_lines=sum(1 for line in open('/home/2016/lcolom2/public_html/cgi-bin/user'))
i=0
for line in f:
	if friendName==None:
		print "Something went wrong..."
		break
	elif friendName.splitlines()[0]==lines_list[i].splitlines()[0]:
		i+=2
		fullName=lines_list[i]
		i+=1
		jobDescription=lines_list[i]
		break
	elif 0<=i<num_lines:
		i+=4
	else:
		break

print "<center><h3><mark>Full name: %s</mark> </h3></center>"%(fullName)
print "<center><h3><mark>Job Description: %s</mark> </h3></center>"%(jobDescription)

print "<br>"


print "		<td><center><form action=\"http://cgi.cs.mcgill.ca/~dzhang52/var/www/cgi-bin/dashboard.py\" method=\"get\">"
print "		<input type=\"radio\" name=\"username\" value=\"%s\" checked>"%(username)
print "		<input type=\"submit\" value=\"Go back to dashboard!\" />"
print "		</form></center></td>"

print "<CENTER><MARK><a href=\"http://cgi.cs.mcgill.ca/~jchen169/welcomePage.html\">Logout</a></MARK></CENTER>"

print "</body>"
print "</html>"
