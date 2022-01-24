'''n, m = input().split()
n = int(n)
m = int(m)

if n == m:
  print (n+1)

if n > m:
    for i in range(m + 1, n + 2):
        print(i)

if m > n:
    for i in range(n + 1, m + 2):
        print(i)'''

'''n, p = input().split()
print(p)'''


'''r, S = input().split()

r=int(r)
S=int(S)

R = 2*S - r

print(R)'''

'''n = int(input())
x = 0
for i in range(n):
    q, y = input().split()
    x += float(q) * float(y)

print(x)'''


'''
while True:
    try:
        a = input().split()
        a = int(a[0]) - int(a[1])
        a = abs(a)
        print(a)
    except EOFError:
        break
'''
