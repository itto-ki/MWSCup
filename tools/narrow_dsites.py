# -*- coding: utf-8 -*-
import re


# "WordPress x.x-beta" とかには対応していない
def sort_by_wp_ver(d):
    wp_list = []
    for x in d:
        if x[1]["WordPress"] and re.match("(^WordPress \d+\.\d+\.\d+$)|(^WordPress \d+\.\d+$)", x[1].get("meta_generator",'')):
            wp_list.append((x[0], x[1]["meta_generator"].replace(',','').split()[1]))

    wp_list.sort(key=lambda s: map(int, s[1].split('.')))
    return wp_list

d=eval(open('test.log','r').read())
#import pdb; pdb.set_trace()
wp_list = sort_by_wp_ver(d)
for x in wp_list:
    print x
