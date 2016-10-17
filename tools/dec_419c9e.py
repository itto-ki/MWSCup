import string
import os
import sys
from base64 import b64decode
import ctypes

# e: encrypted message
e = 'GeB57VGaerHM0y8Wg73sZE^gpfmCpDPAYUBCIU32ahwKDKje/^BNlnav4u9hs^Gwo9GQq7L3XXs6AKoHPvVF/DPSGJC8'

# os check
if os.name != 'nt':
    print 'Sorry, this script cannnot be run on non Windows system'
    sys.exit()

# decode arranged base64
custom_table = 'GKLMopqr6vQBRSwxyz0H1234ZabTcdefg789^/CDAENOPUIVWYJhijklXstu5mnF'
b64_table = string.uppercase + string.lowercase+string.digits + '+/'
e = e.translate(string.maketrans(custom_table, b64_table))
e = b64decode(e)


# TODO: decrypt RC4


# decompress LZNT1 using ntdll.RtlDecompressBuffer
length = len(e)
final_size = ctypes.c_ulong(0)
uncompressed = ctypes.create_string_buffer(length * 40)
workspace = ctypes.create_string_buffer(length * 40)
ctypes.windll.ntdll.RtlDecompressBuffer(2, uncompressed, length * 3, ctypes.c_char_p(e), length, ctypes.byref(final_size))

# print decrypt result
print 'base64 decoded:',e.encode('hex')
for i in range(0, final_size.value):
	print (uncompressed[i]),
print ""
