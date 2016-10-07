# MWSCup

# data
* alexa.lst
    * Alexa top 500のリスト(http://付き)
* data/alexa\_one\_million.lst
    * Alexaのリスト100万件(05-Oct-2016, http://なし)
```
$ (for i in {0..199}; do (curl -s http://listofdomains.org/alexa/alexa_$i.html | sed -n -e '/^<tr><td>[0-9]\+<\/td><td><a href="[^"]\+">/p' | sed -e 's/<\/*[a-z]\+>//g' | sed -e 's/[0-9]\+<a href="[^"]\+">//g'); done;) > alexa_one_million.lst
```
* search\_keywords\_en.lst
    * pagetrafficからとってきた人気キーワードリスト
* suspiciousdomains\_High.txt
    * ドメインブラックリスト(高リスク)
    * https://isc.sans.edu/suspicious\_domains.html
* suspiciousdomains\_Low.txt
    * ドメインブラックリスト(中リスク)
    * URL同上
* suspiciousdomains\_Medium.txt
    * ドメインブラックリスト(低リスク)
    * URL同上

# tools
* crawler.py
    * AlexaTop500のURLを抽出し、ファイルへ出力する
* gethtml.py
    * URLを与えると、そのページのHTMLをファイルへ出力する
* google\_search.py
    * 第一引数をクエリにしてgoogle.comで100件検索、"This site may be hacked."な結果のタイトルとリンク先を出力する
* javascript\_getter.py
    * URLを与えると、そのベージのjavascriptをファイルへ出力する
* check\_webserver.py
    * 第一引数のURLリスト(alexa 100万件を想定)から1つランダムに選び、HEADでアクセスしてServerヘッダを取得したのち、GETでトップページを取得してmetaのgeneratorを取得するのを100回繰り返した結果を出力する
* narrow\_dsites.py
    * check\_webserver.pyの出力からWordPressのサイトだけ抜き出して、WordPressのバージョンが古い順のリストを出力する

# crawler
* crawl.py
    * Googleから人気検索ワードを検索し、上位100件のWebサイトを訪れる
* google_crawler.py
    * Google検索を行い、上位100件のURLを抽出する
* website_crawler.py
    * Seleniumを用いてWebサイトを訪れる
* IEDriverServer.exe
    * Selenium用のIEDriver
