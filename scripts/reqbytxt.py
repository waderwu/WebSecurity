import requests
import sys, argparse
import re

def req(txtname):
    headers = {}

    with open(txtname,'r') as f:
        content = f.read()
        if "\r\n" in content:
            headerandbody = content.split("\r\n")
        else:
            headerandbody = content.split("\n")
        
    
    method, reqpath, _ =  headerandbody[0].split(" ")

    for i in range(len(headerandbody)):
        if headerandbody[i] =="":
            break
        if ":" in headerandbody[i]:
            l= headerandbody[i].split(":")
            val = l[0]
            key = "".join(l[1:])
            headers[val] = key.strip()
    try:
        data = "\r\n".join(headerandbody[i+1:])
    except:
        data = ""
    
    url = "http://" + headers['Host'] + reqpath
    print data
    print headers
    r = None
    if method == "GET":
        if data == "":
            r = requests.get(url=url, headers=headers)
        else:
            r = requests.get(url=url, headers=headers, data=data)
   

    if method == "POST":
        if data == "":
            r = requests.post(url=url, headers=headers)
        else:
            r = requests.post(url=url, headers=headers, data=data)
    return r

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", help="reqtxt")
    args = parser.parse_args()
    r = req(args.r)
    # print r.text
