# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file
import sys
import os
sys.path.append(os.getcwd() + '/..')

import ssl
from py101.modules.bs4 import BeautifulSoup
import urllib.error
import urllib.parse
import urllib.request

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

html = urllib.request.urlopen(
    'https://py4e-data.dr-chuck.net/known_by_Aden.html', context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
cnt = int(input("Count: "))
pos = int(input("Position: "))

# Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times. The answer is the last name that you retrieve.
for i in range(cnt):
    link = tags[pos-1].get('href', None)
    print(tags[pos-1].contents[0])
    html = urllib.request.urlopen(link, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
