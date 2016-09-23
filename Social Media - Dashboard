#!/usr/bin/python

import cgi, cgitb

form=cgi.FieldStorage()
username=form.getvalue('username')

print "Content-type:text/html\r\n\r\n"
print "<HTML>"
print "<HEAD>"
print "<STYLE>"
print "MARK{"
print "        background-color: white;"
print "        color:black;"
print "}"

print "input[type=submit] {"
print "		background-color: #000000;"
print "		border: none;"
print "		color: white;"
print "		padding: 14px 20 px;"
print "		text-decoration: none;"
print "		margin: 4px 2px;"
print "		cursor: pointer;"
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

print ".hide{"
print "	position:absolute; top:-1px; left:-1px; width:1px; height:1px;"
print "}"
print "</style>"
print "<title>Dashboard</title>"
print "</head>"

print "<body background=\"http://cgi.cs.mcgill.ca/~dzhang52/background_Pattern.jpg\">"

print "<center><h1><mark> Dashboard</mark> </h1></center>"
print "<center><p><mark>Dear wizard, welcome to your awesome dashboard!</mark></p></center>"

print "<table border=\"1\" frame=\"below\" width=\"100%\" bgcolor=\"white\">"
print "<tr>"

print "		<td><center><form action=\"http://cgi.cs.mcgill.ca/~jchen169/makeAFriend.py\" method=\"get\">"
print "		<input type=\"radio\" name=\"username\" value=\"%s\" checked>"%(username)
print "		<input type=\"submit\" value=\"Make a Friend!\" />"
print "		</form></center></td>"

print "		<td><center><form action=\"http://cgi.cs.mcgill.ca/~dzhang52/var/www/cgi-bin/seefriends.cgi\" method=\"get\">"
print "		<input type=\"radio\" name=\"username\" value=\"%s\" checked>"%(username)
print "		<input type=\"submit\" value=\"See Friends!\" />"
print "		</form></center></td>"

print "        <td><center><a href=\"http://cs.mcgill.ca/~jchen169/welcomePage.html\">Logout</a></center></td>"
print "</tr>"
print "</table>"

print "<br>"
print "<br>"
print "<iframe name=\"hiddenFrame\" class=\"hide\"></iframe>"
print "<center><form action=\"./status.py\" method=\"post\" target=\"hiddenFrame\">"
print "<mark>Type your new status update : </mark> <input type=\"text\" name=\"update\">"
print "<input type=\"radio\" name=\"username\" value=\"%s\" checked>"%(username)
print "<br>"
print "<mark>Clic on submit</mark>"
print "<input type=\"submit\" onClick=\"history.go(0)\" value=\"Submit\" />"
print "</form></center>"

print "<center><iframe style=\"background: white;\" src=\"./status.txt\" width=\"60%\" height=\"300\"></iframe></center>"

print "</body>"
print "</html>"
