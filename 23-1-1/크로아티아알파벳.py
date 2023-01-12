def solution(Result):
	bb = list(Result)
	answer = []
	cnt = 0
	# 크로아티아알파벳을 하나로 넣는 작업
	for i in range(len(bb)):  # bb 리스트(입력값)의 길이 만큼 반복
		if bb[i] == 'c' and bb[i+1] == '=':  # 만약에 i가 c이고 그다음 문자가 =라면
			answer.append('c=')
			cnt+=1
		elif bb[i] == '=' and bb[i-1] == 'c': # 만약에 i가 =이고 그 전 숫자가 c이면 pass
			continue
		if bb[i] == 'c' and bb[i + 1] == '-':  # 만약에 i가 c이고 그다음 문자가 -라면
			answer.append('c=')
			cnt+=1

		elif bb[i] == '-' and bb[i - 1] == 'c':  # 만약에 i가 -이고 그 전 숫자가 c이면
			continue
		if bb[i] == 'd' and bb[i + 1] == 'z' and bb[i+2] == '=':  # 만약에 i가 d이고 그다음 문자가 z라면
			answer.append('dz=')
			cnt+=1

		elif bb[i] == 'z' and bb[i - 1] == 'd' and bb[i-2] == '=':  # 만약에 i가 0이고 그 전 숫자가 1이면
			continue
		if bb[i] == 'd' and bb[i + 1] == '-':  # 만약에 i가 c이고 그다음 문자가 =라면
			answer.append('dz')
			cnt+=1

		elif bb[i] == '-' and bb[i - 1] == 'd':  # 만약에 i가 0이고 그 전 숫자가 1이면
			continue
		if bb[i] == 'l' and bb[i + 1] == 'j':  # 만약에 i가 c이고 그다음 문자가 =라면
			answer.append('lj')
			cnt+=1

		elif bb[i] == 'j' and bb[i - 1] == 'l':  # 만약에 i가 0이고 그 전 숫자가 1이면
			continue
		if bb[i] == 'n' and bb[i + 1] == 'j':  # 만약에 i가 c이고 그다음 문자가 =라면
			answer.append('nj')
			cnt+=1

		elif bb[i] == 'j' and bb[i - 1] == 'n':  # 만약에 i가 0이고 그 전 숫자가 1이면
			continue
		if bb[i] == 's' and bb[i + 1] == '=':  # 만약에 i가 c이고 그다음 문자가 =라면
			answer.append('s=')
			cnt+=1

		elif bb[i] == '=' and bb[i - 1] == 's':  # 만약에 i가 0이고 그 전 숫자가 1이면
			continue
		if bb[i] == 'z' and bb[i + 1] == '=':  # 만약에 i가 c이고 그다음 문자가 =라면
			answer.append('z=')
			cnt+=1

		elif bb[i] == '=' and bb[i - 1] == 'z':  # 만약에 i가 0이고 그 전 숫자가 1이면
			continue
		else:
			pass
		return cnt
# 크로아티아 알파벳 세는 방법
print(solution('ljes=njak'))
