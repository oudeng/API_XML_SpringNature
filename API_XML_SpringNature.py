#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 17 17:24:43 2020
Search in Spring Nature using API by keywords for NIS lab reserch projects.

@author oudeng, Graduate School of Human Sciences, Waseda University

Python program for searching info from Springer Nature via API by XML.
Results includes the title, pdf url and abstract of destination articles. 

https://dev.springernature.com/signup.  
registerred by WasedaID of Ou,DENG, got necessary API.

How to use?
1) Run this program in Python eviroment, including bs4 and requests lib.
2) Input keywords for searching.
3) Searching results will in Python console window.
4) Read in console window directly if not too many results,
   or copy contents to any other more confortable browsers.
5) Copy url of artitle you like in results, use broswer to read PDF.
 
Can use for other API?
Yes. By modifying base_url, api_key, total and content identification tags.
Just confirm the url you try in other API. 

Can for JSON?
No, this programe for XML only.

"""

from bs4 import BeautifulSoup as bs
import requests

def getXML(url):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "Scraping Errors. Oooop!!"

def spList(total): 
    S=1 
    P=100
    if total%P != 0:
        s = list(range(S, total//P*P, P)) + [total//P*P+1]
        p = list([P]*(len(s)-1)) + [total%P]
    else:
        s = list(range(S, total//P*P, P)) 
        p = list([P]*len(s))
                 
    # print(s)
    # print(p)
    return s, p


def main():
    base_url = "http://api.springernature.com/metadata/pam?q=keyword:"
    api_key = "&api_key=<put your api_key here as following comment.>" 
    #Please register at SpringerNature as the following url for your API key.
    # https://www.springernature.com/gp/campaign/librarian-covid-tdm?sap-outbound-id=64AF2B62DCE26C591DAA9263090CDAF763E0CD1F
    
    #input keywords to search in API, url_1 for confirm 'total' value    
    keywords = input("Input '+' in searching keywords:    ")
    url_1 = base_url + keywords + api_key
    xml_1 = getXML(url_1)
    soup = bs(xml_1,'html.parser')
    total = int(soup.find('total').string)
    
    print('Search Results Totally =',total)
    
    s, p = spList(total)
    
    for i in range(len(s)):
        url = base_url + keywords + '&s=' + str(s[i]) + '&p=' + str(p[i]) + api_key
        xml = getXML(url)
        soup = bs(xml, "html.parser")
        titles = soup.find_all('dc:title')
        urls = soup.find_all('prism:url')
        abstracts = soup.find_all('p')
        
        for j in range(len(titles)):
            print(titles[j].string,'\n', 
            urls[j].string, '\n', 
            abstracts[j].string,'\n','\n')
          
    print('Total=',total)
    
main()


"""
コメント：

1。Python Requests とBeautifulSoupライブラリの組合せ、Anaconda-Python環境であれば楽にできる。
2。getXML(url)関数は、指定URLに対し、内容をRequestするだけ。
　Try-Exceptの組合せは、異常処理するため、汎用型Code。良い習慣を覚えた。
3。spList(total)関数は、検索結果総数total変量に対し、sとpのLIST生成。
　目的は、ページ分けてXML結果を取得。SpringerNature APIは、pが最大100。
4。main（）関数には、主役がBeautifulSoupのXML解析、その結果を表示。
　研究目的のため、title, url(後ほど該当論文のPDFをDLするため),abstractだけで良いと思う。
5。次期、検索結果をPython webbrowserで表示か、PDF打ち出しか、試してみる。


他参考例：
　BeautifulsoupでXMLからテキスト取得
　https://eieito.hatenablog.com/entry/2019/10/05/203105
 base = 'http://iss.ndl.go.jp/api/sru'
 payload = {
    'operation': 'searchRetrieve'
    , 'recordSchema': 'dcndl'
    , 'onlyBib': 'true'
    , 'maximumRecords': '20'
    , 'query': '''creator exact "コードウェイナー・スミス 著"'''
 }

r = requests.get(base, params=payload)
 
"""
    





