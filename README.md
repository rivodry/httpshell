# Httpshell
A reverse shell over http
# How it works
The client sends a GET request to the server,  when a command is given from the server side and the client makes a request it gets the command as the content and executes the command. This is followed by a post request from the client to the server, which posts the output of the command.

