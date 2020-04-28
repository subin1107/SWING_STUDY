import random

rec=[] #최고 기록을 담아줄 리스트
nrec=[] #최고 기록의 이름을 담아줄 리스트



def readrec(): #이전의 기록을 파일에서 가져오는 함수
    rec.clear()
    nrec.clear()
    f=open("C:/Users/btsiu/Desktop/swing.txt",'r') #파일에 있던 내용 기록 읽어오기 위해 swing.txt 문서 열기
    lines=f.readlines()
    for i in range(0, len(lines)): #각 라인을 읽어옴
            nr=lines[i].split(':') #각라인을 : 앞뒤로 나눈 뒤
            nrec.append(nr[0]) #앞부분은 닉네임이므로 nrec리스트에
            rec.append(int(nr[1])) #뒷부분은 기록이므로 rec리스트에 삽입
    f.close()

def writerec(): #기록 파일에 저장하는 함수
    f=open("C:/Users/btsiu/Desktop/swing.txt", 'w') #파일에 내용 기록 추가하기 위해 swing.txt 문서 열기
    for i in range(0,len(rec),1):
        f.write((nrec[i])+str(':')+str(rec[i])) #순위대로 (닉네임:기록) 읽고 저장
        f.write('\n')
    f.close()   


readrec() #게임 시작 전 파일에서 기록을 가져오는 함수 호출

while True: #무한 루프

    answer=random.randint(1,100) #1~100 중에서 랜덤 숫자(정답) 선택

    
    fir=1 #범위 중 제일 작은 숫자. 1부터 선택 가능하므로 1으로 지정
    last=100 #범위 중 제일 큰 숫자. 100까지 선택 가능하므로 100으로 지정
    count=1


    print("UP & DOWN 게임에 오신 걸 환영합니다~",end=' ')
    print("1. 게임시작 2. 기록확인 3. 게임종료",end=' ')
    num=int(input(">> ")) 

    if num==1: #게임 시작 선택시
       while (count<11): 
            print("%d번째 숫자 입력(%d~%d)" %(count,fir,last))
            cha=int(input("")) #도전 숫자 입력

            if cha<answer and cha>fir: #정답보다 숫자가 작고 가능 범위 안의 숫자면
                print("UP") #UP 출력
                fir=cha #답으로 가능한 숫자의 범위 시작을 cha로 변경
                count+=1 #도전 횟수 증가
            elif cha>answer and cha<last: #정답보다 숫자가 크고 가능 범위 안의 숫자면
                print("DOWN") #DOWN 출력
                last=cha  #답으로 가능한 숫자의 범위의 마지막을 cha로 변경  
                count+=1 #도전 횟수 증가
            elif cha>answer or cha<fir: #답으로 가능한 숫자의 범위를 벗어남 => #1번 피드백: 도전 횟수 증가 X
                print("범위에 맞는 숫자를 입력해주세요") 
            elif cha==answer: #정답이라면
                print("정답입니다")
                print("%d번째 만에 맞췄습니다" %(count))  #도전 횟수를 출력해 몇번째 기록인지 출력
                if len(rec)==0:  #처음 기록은 무조건 최고 기록이 됨
                    print("최고 기록입니다")
                    print("닉네임을 입력하세요")
                    maxn=(input(">> ")) #닉네임 받아준 뒤에
                    rec.append(count) #최고기록을 담아주는 리스트 rec에 기록을 등록
                    nrec.append(maxn) #최고 기록을 가진 닉네임을 담는 리스트 nrec에 기록을 등록
                    break
                elif(rec[0]>count): #최고 기록보다 단축했을시
                    print("최고 기록입니다")
                    print("닉네임을 입력하세요")
                    maxn=(input(">> ")) #최고 기록일 때 이름 입력
                    rec.insert(0, count)   #최고 기록 리스트에서 제일 첫번째 위치에 데이터 삽입
                    nrec.insert(0, maxn) #최고 기록을 가진 닉네임을 담는 리스트 제일 첫번째 위치에 데이터 삽입
                    break
                else:
                    break
            if count==11 and cha!=answer: #10번 시도 후에 정답을 맞히지 못했을 떄 출력
                print("GAME OVER! 입력 횟수를 초과하였습니다")     
                break        
    
            
    elif num==2: #기록 확인
        print("rank/name/score")
        for i in range(0,len(rec),1):
            print("%d %s %d" %(i+1,nrec[i],rec[i])) #기록 출력

    elif num==3: #게임 종료
        writerec() #게임종료시 파일에 기록을 입력하는 함수 호출
        break