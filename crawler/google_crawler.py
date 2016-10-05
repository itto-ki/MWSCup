from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.ie.webdriver import WebDriver


class GoogleCrawler(WebDriver):
    """
    Google検索を行うためのクローラ
    """

    def __init__(self, driver):
        super().__init__(driver)
        self.delete_all_cookies()

    def search(self, query, num=100):
        """
        検索をする
        qurery: 検索ワード
        num   : 検索結果出力数
        """
        cmd = 'https://www.google.com/search?num=' + str(num) + '&gl=us&hl=en&gws_rd=cr&q='
        url = cmd + query
        self.get(url)

    def cite_website_urls(self):
        """
        検索結果から各WebサイトのURLを取り出す
        たまにURL以外のゴミが入る
        """
        html = self.page_source
        soup = BeautifulSoup(html, 'html.parser')
        site_list = []
        for anchr in soup.find_all('a'):
            url = anchr.get('href')
            if url.startswith('http://www.google.com'):
                try:
                    site_list.append('http://' + url.split('/')[8])
                except IndexError:
                    pass
        return site_list
