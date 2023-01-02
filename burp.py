import requests
import urllib

url = "http://whilsec.co"
def find_nth_overlapping(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+1)
        n -= 1
    return start

while 1:
    proxy = {"http":"http://127.0.0.1:8080"}
    r = requests.get(url, proxies=proxy)
    html = "<!DOCTYPE html>"
    htmlcharset = r.text.find(html)
    begin = r.text[0:20]
    dup = find_nth_overlapping(r.text,begin,2)
    print(r.text[0:dup])
