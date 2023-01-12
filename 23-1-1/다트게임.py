def solution(dartResult): 
	bb=list(dartResult) # dartResult를 리스트 bb로 만들어 각 자리수 숫자를 비교함
	answer = [] # 정답(숫자) 리스트 
	d = [] # 1,0으로 분리되어 있으면 10으로 만들어 리스트 d에 넣기

# 10을 한숫자로 넣는 작업
	for i in range(len(bb)):  # bb 리스트(입력값)의 길이 만큼 반복
		if bb[i] == '1' and bb[i+1] == '0':  # 만약에 1이고 그다음 숫자가 0이면 
			d.append('10') # d에 10이으로 넣기
		elif bb[i] == '0' and bb[i-1] == '1': # 만약에 i가 0이고 그 전 숫자가 1이면 
			continue # 건너뛰기
		else: # 그 나머지는?
			d.append(bb[i]) # 그냥 i에 값 넣기

#10을 하나의 숫자로 넣은 후에 작업/ 보너스 작업
	for i in range(1,len(d)): # 1부터 d의 길이(10이 정제 되어있는 리스트)만큼 반복하기.
		if d[i] =='S': # 만약에 d의 i번째 값이 S 라면
			answer.append(int(d[i-1])) # 정답에 그 앞에 있는 값에 그대로,
		elif d[i] == 'D': #  만약 D 이면  
			answer.append(int(d[i-1])**2) # 정답에 그 앞에 있는 값에 2제곱
		elif d[i] =='T': # 만약 T 이면
			answer.append(int(d[i-1])**3) # 젇답에 그 앞에 있는 값이 3제곱

#옵션은 *이나 # 중에 하나
		if d[i] =='*': # 만약에 별표면?
			if len(answer)>=2: # answer 의 길이가 2 이상 이면 
				answer[-1]=answer[-1]*2 # answer에 수 곱하기 2
				answer[-2]=answer[-2]*2 # answer에 마지막에서 두번째 값 곱하기 2 넣기
			else: 
				answer[-1]=answer[-1]*2 # 그 나머지는 마지막 값에 곱하기 2
		elif d[i] == '#': # 만약에 ;#' 면(아차상)이면
			answer[-1]=answer[-1](-1) #맨 뒤에 값에 곱하기 -1
	return sum(answer)
