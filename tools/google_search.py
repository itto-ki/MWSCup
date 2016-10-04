from bs4 import BeautifulSoup
from subprocess import Popen, PIPE
import shlex
import sys
import urllib

p = r'curl "'
url_p = r'https://www.google.com/search?num=100&hl=en&q='
#url_s = r'&gs_l=hp.3..0i131k1l7j0j0i131k1l2.2444.2809.0.2968.3.3.0.0.0.0.149.334.2j1.3.0....0...1c.1.64.hp..0.3.331.auRbACUuPlM'
s = r'" -H "Upgrade-Insecure-Requests: 1" -H "Referer: https://www.google.com/" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36" --compressed -s -L'

"""
curl "https://ipv4.google.com/sorry/CaptchaRedirect?captcha=082205&q=CGMSBKPdqYcY_6rNvwUiGQDxp4NLV8I8WGxGA6tncX8ATUdppZ__LrQ&continue=https"%"3A"%"2F"%"2Fwww.google.com"%"2Fsearch"%"3Fnum"%"3D100"%"26biw"%"3D835"%"26bih"%"3D1323"%"26q"%"3Doops"%"2Bpisces"%"26oq"%"3Doops"%"2Bpisces"%"26gs_l"%"3Dserp.3...2222.7292.0.7387.24.19.0.0.0.0.132.1570.13j4.17.0....0...1c.1.64.serp..9.9.854...0j0i22i30k1j0i22i10i30k1j0i131k1j0i67k1j0i10i67k1j33i160k1.hZoTsxyUapU&submit="%"E9"%"80"%"81"%"E4"%"BF"%"A1" -H "Upgrade-Insecure-Requests: 1" -H "Referer: https://ipv4.google.com/sorry/IndexRedirect?continue=https://www.google.com/search"%"3Fnum"%"3D100"%"26biw"%"3D835"%"26bih"%"3D1323"%"26q"%"3Doops"%"2Bpisces"%"26oq"%"3Doops"%"2Bpisces"%"26gs_l"%"3Dserp.3...2222.7292.0.7387.24.19.0.0.0.0.132.1570.13j4.17.0....0...1c.1.64.serp..9.9.854...0j0i22i30k1j0i22i10i30k1j0i131k1j0i67k1j0i10i67k1j33i160k1.hZoTsxyUapU&q=CGMSBKPdqYcY_6rNvwUiGQDxp4NLV8I8WGxGA6tncX8ATUdppZ__LrQ" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36" --compressed
"""

def pread(cmd):
    p = Popen(shlex.split(cmd),stdout=PIPE)
    return p.communicate()[0]

query = urllib.quote(sys.argv[1])

cmd = p + url_p + query + s#url_s + s
data = pread(cmd)
#data = open('google_dbg', 'r').read()

soup = BeautifulSoup(data, "html.parser")
results = soup.find_all('div', class_="rc")

# save search result for debugging
if len(results) == 0:
    img_path = "https://ipv4.google.com"+ soup.find("img").get("src")
    print data
    open('captcha.jpg','wb').write(pread(p + img_path + s))
    sorry_q = soup.find("form").find_all("input", attrs={"name":"q"})[0].get("value")
    sorry_continue = soup.find("form").find_all("input", attrs={"name":"continue"})[0].get("value")
    sorry_submit = soup.find("form").find_all("input", attrs={"name":"submit"})[0].get("value")
    sorry_captcha = raw_input()
    print pread(p + r"https://ipv4.google.com/sorry/CaptchaRedirect?" + "captcha="+ sorry_captcha + "&q=" + sorry_q + "&continue=" + sorry_continue + "&submit=" + sorry_submit + s + r' -H "Referer: '+'https://ipv4.google.com/sorry/IndexRedirect?continue='+sorry_continue+r'&q='+sorry_q+r'"')
    #open("google_dbg_cap","w").write(data)


print "[info] Got",len(results),"result."
for x in results:
    hacked_flag = "This site may be hacked." in str(x)
    for y in x.find_all("a"):
        if hacked_flag and "rwt" in str(y.get("onmousedown")) and not y.get("class"):
            print repr(y.string), y.get("href")
