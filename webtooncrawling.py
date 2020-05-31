import urllib.request
from bs4 import BeautifulSoup
import os #모듈 불러오기
import re #정규표현식 사용을 위한 re모듈

#소녀의 세계 웹툰 페이지 요청 및 파싱
html=urllib.request.urlopen("https://comic.naver.com/webtoon/list.nhn?titleId=654774&weekday=mon") 
result=BeautifulSoup(html.read(),"html.parser") 

#HTTP Error 403: Access Denied 에러 우회
opener=urllib.request.build_opener()
opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
urllib.request.install_opener(opener)

#웹툰 제목 추출 과정
name =  result.find("div", {"class": "detail"}).find("h2")
name = re.sub('<.+?>', '', str(name)) #정규표현식(re.sub) 이용
name=str(name).split()[0]+" "+str(name).split()[1]

#웹툰 제목으로 디렉토리 생성
os.chdir("C:/Users/btsiu/Desktop/")
os.mkdir(name)
print(name+" 디렉토리 생성 완료")

#웹툰의 각 회차의 주소 추출
title = result.findAll("td",{"class":"title"})

#각 회차마다 지행
for t in title:
    #소녀의 세계 각 회차별 웹툰 요청 및 파싱
    html1=urllib.request.urlopen("http://comic.naver.com"+t.a['href'])
    result1=BeautifulSoup(html1.read(),"html.parser")

    webimg=result1.find("div", {"class","wt_viewer"}).findAll("img")#웹툰 이미지 추출 과정

    #웹툰 각 회차별 제목 추출
    epi=result1.find('h3')
    epit=re.sub('<.+?>', '', str(epi))

    os.chdir("C:/Users/btsiu/Desktop/%s"%(name))  #소녀의 세계 디렉토리로 이동
    os.mkdir(epit) #소녀의 세계 디렉토리 안에 해당 회차 제목 디렉토리 생성
    os.chdir("C:/Users/btsiu/Desktop/%s/%s"%(name,epit))  #해당 회차 제목 디렉토리로 이동
    
    #해당 회차 웹툰 이미지 저장
    num=1
    for w in webimg:
        url=w.get("src")
        save=str(num)+".png"
        urllib.request.urlretrieve(url,save)
        num=num+1
    print(epit+" 다운로드 완료")
  
    os.chdir("..")   #이전 디렉토리(소녀의 세계 디렉토리)로 이동

print(name+" 다운로드 완료") #모든 회차의 웹툰 이미지 저장 완료 후 소녀의 세계 다운로드 완료 출력