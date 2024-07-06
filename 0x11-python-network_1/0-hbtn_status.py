#!/usr/bin/python3
""" A Python script that fetches
https://alx-intranet.hbtn.io/status"""

if __name__ == '__main__':
    
    import urllib.request as model
    
    with model.urlopen('https://alx-intranet.hbtn.io/status') as response:
        res_result = response.read()
        print('\t - type: {}'.format(type(res_result)))
        print('\t - content: {}'.format(res_result))
        print('\t - utf8 content: {}'.format(res_result.decode('utf-8')))