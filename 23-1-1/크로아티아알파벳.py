c = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z='] # 크로아티아알파벳을 리스트에 넣기
a = input() #a는 값을 입력받는다.

for i in c: # 크로아티아알파벳을 하나씩 넣으면서 실행
    a = a.replace(i, '*') # replace 함수를 사용하여 문자열을 변수에 저장하지 않고 바로 계산할 수 있다,  크로아티아 알파벳 하나하나를 *로 치환하고, 그대로 계산
print(len(a))
