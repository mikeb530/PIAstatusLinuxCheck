from bs4 import BeautifulSoup

import requests
import subprocess
import signal
import os
from datetime import datetime as dt
import time

counter = 100
process = 'transmission'

while True:
    url = 'https://www.privateinternetaccess.com/?now=' + str(dt.now())

    r = requests.get(url)

    data = r.text
    protected_vpn = False

    soup = BeautifulSoup(data, 'lxml')

    for link in soup.find_all('li'):
        if str(link.text).find('You are protected by PIA'):
            protected_vpn = True
            break

    if not protected_vpn:
        proc = subprocess.Popen(
            ['pgrep', process], stdout=subprocess.PIPE)

        for pid in proc.stdout:
            os.kill(int(pid), signal.SIGTERM)

        print('Unprotected killed processes')

    else:
        if counter >= 100:
            print('You are protected ' + str(dt.now()))
            counter = 1

    counter = counter + 1
    time.sleep(15)
