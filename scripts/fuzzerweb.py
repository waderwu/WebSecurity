import requests

def parser_header(header):
    tmpheaders = header.split("\n")
    headers = {}
    
    for i in range(len(tmpheaders)):
        if ":" in tmpheaders[i]:
            l= tmpheaders[i].split(":")
            val = l[0]
            key = "".join(l[1:])
            headers[val] = key.strip()
    return headers

if __name__ == "__main__":
    header="""POST /alien_sector.php HTTP/1.1
Host: 138.68.228.12
Connection: keep-alive
Content-Length: 22
Cache-Control: max-age=0
Origin: http://138.68.228.12
Upgrade-Insecure-Requests: 1
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Referer: http://138.68.228.12/alien_sector.php
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7
Cookie: PHPSESSID=etvoocnk2flt9oau5fheo8vcc4
"""
    url = "http://138.68.228.12/alien_sector.php"
    url = "http://www.sjtu.edu.cn"
    headers = parser_header(header)

    payloads = """0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,\-./:;<=>?@[\]^_`{|}~ \t\n\r\x0b\x0c"""
    with open("out","w") as f:
        for i in payloads:
            s = requests.Session()
            proxies = {'http': 'http://127.0.0.1:1080'}

            r = s.get(url=url, headers=headers)
