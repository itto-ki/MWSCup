from bs4 import BeautifulSoup
import urllib.request

urls_alexa = []
page = 20

f = open('alexa.lst', 'w')

# AlexaTop500の各ページ概要のリンクを取得
for i in range(page):
    html = urllib.request.urlopen('http://www.alexa.com/topsites/global;' + str(i))
    soup = BeautifulSoup(html)
    print('Page {}'.format(i))

    domain = 'http://www.alexa.com'

    for divs in soup.find_all('li'):
        link = divs.find('a').get('href')
        if link.startswith('/siteinfo'):
            if not link.strip('/').endswith('siteinfo'):
                urls_alexa.append(domain + link)
                print('Getting a link: {}'.format(domain + link))

# Top500のurlをファイルへ書き出し
orig_urls = []
for i, url in enumerate(urls_alexa):
    print('[{}/{}] Getting a link from {}'.format(i, len(urls_alexa), url))
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html)
    for link in soup.find_all('a'):
        href = link.get('href')
        if href:
            if href.startswith('http://web.archive.org/'):
                lnk = href.split('*')[1][1:] + '\n'
                if lnk.startswith('http'):
                    f.write(lnk)

f.close()
