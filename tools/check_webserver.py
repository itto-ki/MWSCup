# -*- coding: utf-8 -*-
import sys
import urllib2
import re
import shlex
import pprint
import random
from subprocess import Popen, PIPE
from bs4 import BeautifulSoup

cURL_OPTIONS = "-m 10 "

def getHead(host):
    return Popen(shlex.split("curl -sLI "+ cURL_OPTIONS + host), stdout=PIPE).communicate()[0]

def getReq(host):
    return Popen(shlex.split("curl -sL " + cURL_OPTIONS + host), stdout=PIPE).communicate()[0]

def main():
    args = sys.argv

    if len(args) != 2:
        print >> sys.stderr, "Usage: %s [filename of domain list]" % args[0]
        sys.exit()

    url_list = open(args[1], 'r').read().split()

    result = []
    pattern = re.compile(r"Server: ")
    #for host in url_list:
    for i in range(100):
        host = random.choice(url_list)
        dic = {}
        print >> sys.stderr, "Looking up", host
        head = getHead(host)

        # "www."をつけてリトライ
        if len(head) == 0:
            host = "www." + host
            print >> sys.stderr, "  Retrying:", host
            head = getHead(host)
            if len(head) == 0:
                continue

        # Server ヘッダ
        h = pattern.split(str(head))
        if len(head) > 0 and len(h) == 2:
            server = h[-1].split('\r\n')[0]
            dic["Server"] = server

        data = getReq(host)
        soup = BeautifulSoup(data, "html.parser")
        meta_generator = soup.find("meta", attrs={"name":"generator"})
        if meta_generator:
            dic["meta_generator"] = meta_generator.get("content")
        dic["WordPress"] = True if "wp-content" in data else False

        result.append((host,dic))

    pprint.pprint(result)

if __name__ == '__main__':
    main()
