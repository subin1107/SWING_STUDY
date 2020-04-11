import random

rec=[] #기록을 담아줄 리스트

while True: #무한 루프
    answer=random.randint(1,100) #1~100 중에서 랜덤 숫자(정답) 선택
    
    fir=1 #범위 중 제일 작은 숫자. 1부터 선택 가능하므로 1으로 지정
    last=100 #범위 중 제일 큰 숫자. 100까지 선택 가능하므로 100으로 지정
    max=100 #최고 기록을 세어줄 숫자. 처음 시도는 무조건 최고 기록이 나와야 함으로 10보다 큰 수 지정 

    print("UP & DOWN 게임에 오신 걸 환영합니다~",end=' ')
    print("1. 게임시작 2. 기록확인 3. 게임종료",end=' ')
    num=int(input(">> ")) 

    if num==1: #게임 시작 선택시
        for i in range(1,11): #총 10번의 기회를 줌
            print("%d번째 숫자 입력(%d~%d)" %(i,fir,last))
            cha=int(input("")) #도전 숫자 입력

            if cha<answer and cha>fir: #정답보다 숫자가 작고 가능 범위 안의 숫자면
                print("UP") #UP 출력
                fir=cha #답으로 가능한 숫자의 범위 시작을 cha로 변경
            elif cha>answer and cha<last: #정답보다 숫자가 크고 가능 범위 안의 숫자면
                print("DOWN") #DOWN 출력
                last=cha  #답으로 가능한 숫자의 범위의 마지막을 cha로 변경  
            elif cha>answer or cha<fir: #답으로 가능한 숫자의 범위를 벗어남
                print("범위에 맞는 숫자를 입력해주세요")
            elif cha==answer: #정답이라면
                print("정답입니다")
                print("%d번째 만에 맞췄습니다" %(i))  #도전 횟수를 출력해 몇번째 기록인지 출력
                if(max>i): #최고 기록보다 단축했을시
                    print("최고 기록입니다")
                    max=i #최고 기록을 수정
                rec.append(i) #점수 등록 
                break
            else: print("GAME OVER! 입력 횟수를 초과하였습니다") #10번 시도 후에 정답을 맞히지 못했을 떄 출력 
    elif num==2: #기록 확인
        rec.sort() #순위 정렬
        for i in range(len(rec)):
            print("%d위 %d" %(i+1, rec[i])) #기록 출력


    else: #게임 종료
        break                  