#head = 문자 , 최소한 한글자 이상
#number = 한글자에서 최대 다섯 글자 사이 숫
#tail  = 나머지 부분, 숫자나 null 값

# if head 대소문자 구분 없음, 사전 순 정렬
#   if head 같으면 number부분 정렬
#       if head, number 같으면 원래 입력 주어진 순서 유지-> 아무것도 안한다.
# 딕셔너리 키를 오름차순 정렬할 수 있다.
files = ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]
#files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
data = []
head = ""
number = ""
tail = ""
num = 0
for file in files : #문자열 하나 요소 반복
    for i in range(len(file)):
        if file[i].isdigit():#i 값이 문자열이라면?
            head = file[:i]#head 리스트에 값 넣기
            number = file[i:]
            for j in range(len(number)): # number의 길이만큼 반복 하나씪 j에 넣기
                if number[j].isalpha(): # j의 값이 문자열이라면?
                    tail = number[j:] #마지막값은 NUMBER의 숫자 다음
                    number = number[:j]#number값은 숫자가나올때까지만 출력
                    break #숫자 찾으면 문자 종료
            break
                #if sp_number[j].isdigit(): #number[j] 가 숫자라면
                    #number = sp_number#
                    #tail = number[:j]
    #print(head_idx,head)
    #print(number_idx,number)
    #print(tail_idx,tail)
    #number= int() number을 int 형으로 변환하면 0이 출력된다.
    data.append((head,number,tail)) # data리스트에 값 추가
sorted_data = sorted(data,key = lambda x: x[0]) # 우선순위를 기준으로 정렬 # 01이 1보다 우선이다..
print(sorted_data)
for item in sorted_data:
    print(item[0],item[1],item[2])
    #while i.isdigit() is False: #문자열 요소가 문자열일때까지 반복하고, 문자열이면 출
        #while i.isdigit is True:  #i.isdigit가 문자인경우
    #if  #head 나누기, head는 문,
    #print(file)

# 일단 files 함수의 순서를 설정한다.
#files_sorted = {i: files[i] for i in range(len(files))}
#print(files_sorted) # 리스트를 딕셔너리로 변경
#print(sorted(files_sorted.items(),key=lambda x:x[1])) # value 값을 기준으로 정렬
# head
# number
# tail
