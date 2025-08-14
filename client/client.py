
from urllib import request, parse

import time

while True:
    command = request.urlopen(f"http://localhost:5000").read().decode()
    print(command)
    time.sleep(1)
