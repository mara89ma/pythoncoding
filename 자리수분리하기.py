number = 1023
sum = 0
num_list= list(map(int,str(number)))
# print(num_list) # 자리수 분리하여 출력
for i in num_list:
    print(i)
    sum +=i
print(sum)
