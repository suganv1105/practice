# HTML is following
print("Content-Type: text/html")
# blank line, end of headers
print()
print("<title> This is a CGI script output</title>")
print("<h1>This is my first CGI script</h1>")
print("Hello, JavaTpoint!")

import cgi
cgitb.enable()

import cgitb
cgitb.enable(display=0, logdir="logdir")