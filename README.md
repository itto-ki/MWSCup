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
    * https://isc.sans.edu/suspicious_domains.html
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
* scan\_vulnerable\_webserver.py
    * 第一引数のURLリストにHEADでアクセスして、Serverヘッダを出力する
* virustotal.py
    * 第一引数のリストをVirusTotalのURL Searchに投げてpositiveの数を出力する

# crawler
* crawl.py
* google_crawler.py
* website_crawler.py
* IEDriverServer.exe
