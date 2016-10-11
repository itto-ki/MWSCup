# -*- coding: utf-8 -*-

import sys
import urllib2
from StringIO import StringIO
import gzip
import difflib
import re
import random
from bs4 import BeautifulSoup

def detectEncoding(data):
    lookup = ('utf_8', 'euc_jp', 'euc_jis_2004', 'euc_jisx0213',
            'shift_jis', 'shift_jis_2004','shift_jisx0213',
            'iso2022jp', 'iso2022_jp_1', 'iso2022_jp_2', 'iso2022_jp_3',
            'iso2022_jp_ext','latin_1', 'ascii')
    encode = None
    for l in data.splitlines():
        if 'meta' in l:
            for encoding in lookup:
                if encoding in l:
                    encode = encoding
                    break
        if encode:
            break
    if encode == None:
        for encoding in lookup:
            try:
                data = data.decode(encoding)
                encode = encoding
                break
            except:
                pass
    if isinstance(data, unicode):
        return data,encode
    else:
        raise LookupError

def getUrl(url):
    """
    headers = {
        "Pragma": "no-cache",
        "DNT": "1",
        "Accept-Encoding": "gzip, deflate, sdch",
        "Accept-Language": "ja,en-US;q=0.8,en;q=0.6",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive"
    }
    """
    headers = {
        "Accept": "text/html, application/xhtml+xml, image/jxr, */*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "ja-JP",
        "Connection": "Keep-Alive",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393"
    }

    req = urllib2.Request(url, headers=headers)
    try:
        r = urllib2.urlopen(req)
    except urllib2.HTTPError as e:
        data = e.readlines()
        for l in data:
            if l.startswith('<img'):
                print l
        return None

    if r.info().get('Content-Encoding') == 'gzip':
        buf = StringIO(r.read())
        f = gzip.GzipFile(fileobj=buf)
        data = f.read()
    else:
        data = r.read()
    return data

def getGoogleCache(url):
    gUrl = "http://webcache.googleusercontent.com/search?q=cache:" + url + "&num=1&strip=0&vwsrc=0"
    return getUrl(gUrl)


def main():
    args = sys.argv

    #url = args[1]
    domain = random.choice(open(args[1], 'r').readlines()).replace('\n','')
    print '---'
    print domain

    #cache_data = '\n'.join(getGoogleCache(url).splitlines()[2:])
    #soup = BeautifulSoup(getUrl(url), "html.parser")
    #print HTMLParser().unescape(soup.find("pre").string).encode('utf-8')
    if not domain.startswith('http'):
        url = 'http://'+domain
    else:
        url = domain
    data = getUrl(url)
    data = detectEncoding(data)[0].encode('utf-8')

    """
    print 'original:',len(data)
    print 'cache   :',len(cache_data)
    print 'sub     :',len(data) - len(cache_data)
    g = difflib.unified_diff(cache_data.splitlines(), data.splitlines())
    cnt = 0
    for l in g:
        if cnt > 0:
            cnt -= 1
            print l
            continue
        if l.startswith('+'):
            if "<script" in l.lower() or "<iframe" in l.lower():
                print l
                cnt = 3
    """
    soup = BeautifulSoup(data, "html.parser")
    for x in soup.find_all("script"):
        s = x.get("src")
        if s and s.startswith("http") and not domain in s:
            print "script:",s
    for x in soup.find_all("iframe"):
        s = x.get("src")
        print "iframe:",s

if __name__ == '__main__':
    main()
