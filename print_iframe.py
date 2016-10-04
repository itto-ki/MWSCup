import os
import urllib.request
import threading
from bs4 import BeautifulSoup

f_alexa = open('alexa.lst', 'r')
urls = []

for line in f_alexa.readlines():
    urls.append(line)

def gethtml():
    url = urls.pop()
    hostname = url.split('/')[2].strip('\n')
    #  os.system('mkdir ' + hostname)
    #  f = open(hostname + '/' + hostname + '.html', 'wb')
    print('Getting a html file from {}'.format(url), end='')
    try:
        html = urllib.request.urlopen(url)
        soup = BeautifulSoup(html)
        f_iframe = open('iframes.txt', 'w')
        for iframe in soup.find_all('iframe'):
            #  f_iframe.write(iframe.get('src') + '\n')
            f_iframe.write(iframe.get('src'))
        #  f.write(html.read())
        f_iframe.close()
        #  f.close()
    except:
        #  f.close()
        f_iframe.close()

while True:
    if len(urls) <= 0:
        break
    threading.Thread(target=gethtml).start()
