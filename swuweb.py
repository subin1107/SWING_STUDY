from bs4 import BeautifulSoup

import urllib.request #모듈 불러오기

html=urllib.request.urlopen("http://www.swu.ac.kr/www/swuniversity.html")
result=BeautifulSoup(html.read(),"html.parser") #서울여자대학교 학과 웹페이지 요청 및 파싱

search=result.findAll("a") #모든 a 태그 내용 출력 
print("*** 서울여자대학교 학과 및 홈페이지 정보 ***")
print("학과 \t\t\t\t 홈페이지")

for s in search:
    if "대학원" in s.text or "교육원" in s.text or s.text=="자율전공학부" or s.text=="공동기기실": #학과와 전공만 가져오기 위해 제외
        continue

    else:
        html1=urllib.request.urlopen("http://www.swu.ac.kr"+s["href"]) 
        result1=BeautifulSoup(html1.read(), "html.parser") #각각의 학과, 전공 웹페이지 요청 및 파싱

        search1=result1.find("a",{"class","btn btn_xl btn_blue_gray"}) #각각의 학과, 전공 홈페이지 읽어옴

        print(s.text, end="\t\t\t") #학과 출력
        if not search1: #학과, 전공 홈페이지가 없을 때 존재하지 않는다는 문구 출력
            print("홈페이지가 존재하지 않음")
            
    
        elif "홈페이지" in search1.text: #학과 혹은 전공 홈페이지 존재할 때 url 출력
            print(search1['href'])
        else: #이외의 경우 홈페이지 존재 X 문구 출력
            print("홈페이지가 존재하지 않음")
