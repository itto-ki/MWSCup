# -*- coding: utf-8 -*-
import sys
import urllib2
import re

def main():
    args = sys.argv

    if len(args) != 3:
        pass

    url_list = open(args[1], 'r').read().split()

    pattern = re.compile(r"Server: ")
    for url in url_list:
        print url + ":", 
        req = urllib2.Request(url)
        req.get_methold = lambda : 'HEAD'

        try: 
            res = urllib2.urlopen(req)
            head = res.info()
            h = pattern.split(str(head))
            if len(h) == 2:
                server = h[-1].split('\r\n')[0]
                print server
            else:
                raise
        except:
            print "[Cannot Get Server Infomation]"

if __name__ == '__main__':
    main()
