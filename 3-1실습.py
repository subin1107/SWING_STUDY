from bs4 import BeautifulSoup

import urllib.request

html=urllib.request.urlopen("https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=")
result=BeautifulSoup(html.read(),"html.parser")

search=result.findAll("span",{"class","tit"})

index=0
for s in search:
    index=index+1
    print(index,s.text)