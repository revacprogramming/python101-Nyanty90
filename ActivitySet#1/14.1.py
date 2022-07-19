# Using Web Services
# https://www.py4e.com/lessons/servces
import urllib.request
import urllib.parse
import urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_1550755.xml'
uh = urllib.request.urlopen(url).read()
print('Retrieved', len(uh), 'characters')
tree = ET.fromstring(uh)
results = tree.findall('.//count')
sum = 0
for item in results:
    sum += int(item.text)
print(f"Count: {len(results)}")
print(f"Sum: {sum}")
