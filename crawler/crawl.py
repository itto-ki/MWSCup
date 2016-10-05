import sys
import time
from multiprocessing import Pool
from google_crawler import GoogleCrawler
from website_crawler import WebSiteCrawler


DRIVER_PATH = '/home/itto-ki/Works/IEDriverServer.exe'



def crawl_website(url):
    wsc = WebSiteCrawler(DRIVER_PATH, url)
    time.sleep(3)
    wsc.quit()

words_file = open('search_keywords_en.lst', 'r')
for word in words_file.readlines()
    gc = GoogleCrawler(DRIVER_PATH)
    try:
        gc.search(word)
        website_urls = gc.cite_website_urls()
        p = Pool(6)
        p.map(crawl_website, website_urls)
    except:
        sys.stderr.write('Cannot search for {}'.format(word))
    gc.quit()
