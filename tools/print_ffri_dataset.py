import json
import sys
import pprint


data = open(sys.argv[1], 'r').read()
j = json.loads(data)
#for key in j.keys():
    #print key
pprint.pprint(j)

