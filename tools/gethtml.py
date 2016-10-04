import urllib.request
import threading

f_alexa = open('alexa.lst', 'r')
urls = []

for line in f_alexa.readlines():
    urls.append(line)

def gethtml():
    url = urls.pop()
    f = open(url.split('/')[2].strip('\n') + '.html', 'wb')
    print('Getting a html file from {}'.format(url.split('/')[2]), end='')
    try:
        html = urllib.request.urlopen(url)
        f.write(html.read())
        f.close()
    except:
        f.close()

while True:
    if len(urls) <= 0:
        break
    threading.Thread(target=gethtml).start()
