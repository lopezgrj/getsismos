#!/usr/bin/env python

from lxml import html
import requests
from datetime import datetime
import urllib3
import chardet
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://webserver2.ineter.gob.ni/geofisica/sis/events/sismos.php"

page = requests.get(url, verify=False)
detected = chardet.detect(page.content)
encoding = detected['encoding'] if detected['encoding'] else 'utf-8'
tree = html.fromstring(page.content.decode(encoding))

q = tree.xpath('//a')

file = 'lista_de_sismos.txt'
tfile = 'lastupdate.txt'

a = []
for anchor in reversed(q):
    text = anchor.text_content().strip()
    if text:
        with open(file, 'r', encoding='utf-8') as f:
            if text not in f.read():
                a.append(text)

with open(file , 'a', encoding='utf-8') as myfile:
    for i in a:
	    myfile.write(i+"\n")

with open(tfile,'w', encoding='utf-8') as timefile:
	timefile.write(datetime.now().isoformat())