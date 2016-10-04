import sys
import os
import json
import shlex
from subprocess import Popen, PIPE

p="""
curl "https://virustotal.com/ja/url/submission/" -H "origin: https://virustotal.com" -H "accept-encoding: gzip, deflate, br" -H "accept-language: ja,en-US;q=0.8,en;q=0.6" -H "x-requested-with: XMLHttpRequest" -H "x-csrftoken: null" -H "cookie: __utmt=1; __utma=194538546.2075850495.1474370108.1475234837.1475489880.4; __utmb=194538546.7.10.1475489880; __utmc=194538546; __utmz=194538546.1474370108.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); VT_PREFERRED_LANGUAGE=ja" -H "pragma: no-cache" -H "user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36" -H "content-type: application/x-www-form-urlencoded" -H "accept: application/json, text/javascript, */*; q=0.01" -H "cache-control: no-cache" -H "authority: virustotal.com" -H "referer: https://virustotal.com/" -H "dnt: 1" --data "url=
"""
s='" --compressed -s'

l=open(sys.argv[1], 'r').read().split()

for url in l:
    print url,":",
    res = Popen(shlex.split(p + url + s), stdout=PIPE).communicate()[0]
    res = json.loads(res)

    print res["positives"]
