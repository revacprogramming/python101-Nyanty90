# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import sys
import os
sys.path.append(os.getcwd() + '/..')

from urllib.request import urlopen
from py101.modules.bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

html = urlopen('http://py4e-data.dr-chuck.net/comments_1550753.html', context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags, s = soup('span'), 0
for tag in tags:
    # Look at the parts of a tag
    s += int(tag.contents[0])

print(s)
