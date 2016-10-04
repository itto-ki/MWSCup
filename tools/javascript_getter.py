import os
import urllib.request
from bs4 import BeautifulSoup


def get_js(file_name, url):
    try:
        js = urllib.request.urlopen(url)
        print('\t{}'.format(file_name))
        js_file = open(file_name, 'wb')
        js_file.write(js.read())
    except:
        print('\tFailed!!')
        return
    js_file.close()


def extract_js_url(soup):
    urls = []
    for script in soup.find_all('script'):
        if script.get('src'):
            urls.append(script.get('src'))
    return urls


def make_soup(url):
    try:
        html = urllib.request.urlopen(url)
    except:
        return
    soup = BeautifulSoup(html)
    return soup


def main():
    url_file = open('alexa.lst', 'r')
    os.chdir('./js')
    for url in url_file.readlines():
        hostname = url.split('/')[2].strip('\n')
        soup = make_soup(url)
        if soup:
            js_urls = extract_js_url(soup)
        for i, js_url in enumerate(js_urls):
            print('Getting javascript from {}. No.{}'.format(hostname, i))
            get_js(hostname + '_' + str(i) + '.js', js_url)
            #  js_filename = js_url.split('/')[-1]
            #  get_js(js_filename, js_url)
    url_file.close()


if __name__ == '__main__':
    main()
