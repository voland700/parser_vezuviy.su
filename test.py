from bs4 import BeautifulSoup
import urllib.request
import fake_useragent
import json
import requests
import pathlib
import os
import string
import random
import openpyxl
import datetime

import urllib.parse

ua = fake_useragent.UserAgent()
headers = {"User-Agent":ua.random}
#url = 'https://vezuviy.su/dymohody-i-baki/dymohody-nerzhaveyuschie/homut-nerzh.-aisi-430/'
#url = 'https://vezuviy.su/gotovim-na-vezuvii-ru/gril-pech-ot-shefa/stol-stellazh-primangalnyy-ot-shefa/'
#url ='https://vezuviy.su/gotovim-na-vezuvii-ru/chugunnaya-kostrovaya-chasha-fantastic-o-1000-prestizh/'
#url = 'https://vezuviy.su/gotovim-na-vezuvii-ru/'

url ='https://vezuviy.su/video/dymohody-vezuviy-iz-nerzhaveyuschey-stali.-obzor/'





def randomStr(nrandchars):
    alpha = string.ascii_letters + string.digits
    chars = ''.join(random.choice(alpha) for _ in range(nrandchars))
    return chars


def get_files(link, folder='images'):
    response = requests.get(link, stream=True)
    ext = pathlib.Path(link).suffix
    if not os.path.isdir("upload"):
        os.mkdir("upload")
    if not os.path.isdir("upload/" + folder):
        os.mkdir("upload/" + folder)
    file_name = 'upload/' + folder + '/' + folder + '_' + randomStr(10) + ext
    file = open(file_name, 'bw')
    for chunk in response.iter_content(4096):
        file.write(chunk)
    return file_name


item = dict()
item['url'] = url
item['title'] = None
item['link'] = None
req = urllib.request.Request(url, data=None, headers=headers)
req = urllib.request.urlopen(req)
if req.getcode() != 200:
    exit()
html = req.read()
soup = BeautifulSoup(html, 'html.parser')
item['title'] = soup.find('h1', {'class': 'ty-mainbox-title'}).get_text(strip=True)
link = soup.find('div', {'class': 'cp-video-detailed__video-wrapper'}).iframe['src']


if link.find('?') != -1:
    item['link'] = link.split('?')[0]
else:
    item['link'] = link

print(item)












