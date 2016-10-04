# MWSCup

# data
* alexa.lst
    * Alexa top 500のリスト(http://付き)
* search\_keywords\_en.lst
    * pagetrafficからとってきた人気キーワードリスト
* suspiciousdomains\_High.txt
    * 
* suspiciousdomains\_Low.txt
    * 
* suspiciousdomains\_Medium.txt
    * 

# tools
* crawler.py
    * 
* gethtml.py
    * 
* google\_search.py
    * 第一引数をクエリにしてgoogle.comで100件検索、"This site may be hacked."な結果のタイトルとリンク先を出力する
* javascript\_getter.py
    * 
* scan\_vulnerable\_webserver.py
    * 第一引数のURLリストにHEADでアクセスして、Serverヘッダを出力する
* virustotal.py
    * 第一引数のリストをVirusTotalのURL Searchに投げてpositiveの数を出力する
