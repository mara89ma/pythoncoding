n = 5
a = 2*n+1

for i in range(a//2):
    print(' ' * (a//2 - i), end = '')
    print('1' * (2*i+1))

for i in range(a//2-1):
    print(' ' * (i + 2), end = '')
    print('1' * ((a//2*2)-3-2*i))

