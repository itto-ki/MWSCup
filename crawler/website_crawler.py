import sys
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import *

class WebSiteCrawler(WebDriver):
    """
    任意のWebサイトのためのクローラ
    """

    # Webサイトのドメイン 'http://www.google.com' -> 'www.google.com'
    domain  = ''
    # WebサイトのURL 'http://www.google.com' -> 'http://www.google.com'
    url     = ''
    timeout = 10
    # 既に訪れたことのあるWebサイトを登録しておくとget_childpage_urlsによりURLを抜き出さない
    visited = []

    def __init__(self, driver, url, visited=[]):
        super().__init__(driver)
        self.set_page_load_timeout(self.timeout)
        try:
            self.get(url)
        except:
            sys.stderr.write('Access Error to {}\n'.format(url))
        self.visited = visited

    def get(self, url):
        self.url = url
        self.domain = url.split('/')[2]
        super().get(url)

    def get_childpage_urls(self):
        """
        子ページへのリンクを抽出し、リスト形式で返す
        """
        html = self.page_source
        soup = BeautifulSoup(html, 'html.parser')
        page_list = []
        for anchr in soup.find_all('a'):
            href = anchr.get('href')
            if href is not None:
                try:
                    url = self.make_valid_url(href)
                    if not url in page_list and not url in self.visited:
                        page_list.append(url)
                except ValueError:
                    sys.stderr.write('Invalid URL: {}\n'.format(href))
        return page_list

    def make_valid_url(self, url):
        """
        URLが正しい形式をしていなければ正しい形式に変換して返す
        """
        if url.startswith('http://') or url.startswith('https://'):
            return url
        elif url.startswith('./'):
            return self.url + url[1:]
        elif url.startswith('//'):
            return 'http:' + url
        elif url.startswith('/'):
            return 'http://' + self.domain + url
        else:
            raise ValueError
