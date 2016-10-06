import sys
import time
from multiprocessing import Pool
from google_crawler import GoogleCrawler
from website_crawler import WebSiteCrawler


DRIVER_PATH = '/home/itto-ki/Works/IEDriverServer.exe'


def crawl_website(url):
    wsc = WebSiteCrawler(DRIVER_PATH, url)
    time.sleep(3)
    try:
        wsc.quit()
    except:
        sys.stderr.write('Cannot crawling {}'.format(url))


words_file = open('search_keywords_en.lst', 'r')
for word in words_file.readlines()
    try:
        gc = GoogleCrawler(DRIVER_PATH)
    except:
        continue
    try:
        gc.search(word)
    except:
        sys.stderr('Cannot open {} in GoogleCrawler'.format(word))
        gc.close()
        continue
    try:
        print('Searching now - {}'.format(word))
        website_urls = gc.cite_website_urls()
        try:
            p = Pool(6)
            p.map(crawl_website, website_urls)
            p.terminate()
            p.join()
        except:
            sys.stderr.write('Unkown Error: Process stopeed. killing process')
    except:
        sys.stderr.write('Cannot search for {}'.format(word))
    gc.quit()
