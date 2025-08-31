# Httpshell 🖥️◀️
A reverse shell over http
# Workings
- [server.py](https://github.com/rivodry/httpshell/blob/main/server/server.py) is ran on the attacker's server/PC.
- The [client](https://github.com/rivodry/httpshell/blob/main/client/client.go) sends a POST to the server with the computer's info.
- The attacker can enter a command to be executed, the client gets the command using a GET request and executes it.
- A POST is made to the server with the output of the command
# Custom client
- The client should send a POST to the server with json (client should also check for device details and fill in the SHELL and OS)
- `"info":"Shell: {SHELL} \n OS: {OS}"`
- The client should have a loop sending a GET request to the server, storing the command and executing it, and POSTing the output.
