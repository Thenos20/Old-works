x = int(input())
buses = input().split()
buses.sort()


for o in range(x):
    buses[o] = int(buses[o])

copy = buses.copy()

for i in range(x):
    if buses[i] - 1 == buses[i - 1] and buses[i - 2] == buses[i] - 2:
        copy.remove(buses[i-1])

output = ''

for i in range(x):
    if buses[i] not in copy:
        buses[i] = '-'

for i in range(x):
    output += str(buses[i])+' '

for i in range (x):
    output = output.replace('--', '-')
    output = output.replace('- -','-')
    output = output.replace(' - ','-')
    output = output.replace(' -','-')


print(output)


