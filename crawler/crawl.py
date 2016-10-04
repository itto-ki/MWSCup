import time
from google_crawler import GoogleCrawler
from website_crawler import WebSiteCrawler


DRIVER_PATH = '/home/itto-ki/Works/IEDriverServer.exe'


gc = GoogleCrawler(DRIVER_PATH)
gc.search('malware')
website_urls = gc.cite_website_urls()

for url in website_urls[:3]:
    wsc = WebSiteCrawler(DRIVER_PATH, url)
    time.sleep(3)
    print(wsc.get_childpage_urls())
    wsc.quit()
