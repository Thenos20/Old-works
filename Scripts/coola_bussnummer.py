x = int(input())
buses = input().split()
for o in range(x):
    buses[o] = int(buses[o])
buses.sort()
copy = buses.copy()

#1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
for i in range(x):
    if buses[i] - 1 == buses[i - 1] and buses[i - 2] == buses[i] - 2:
        copy.remove(buses[i-1])

output = ''

for i in range(x):
    if buses[i] not in copy:
        buses[i] = ['-']
for i in range(x):
    output += str(buses[i]) + ' '
for i in range(x):
    output = output.replace(" ['-'] ", '-')
    output = output.replace("['-'] ", '')
    output = output.replace("['-']", '')
    output = output.replace('- -', '-')
    output = output.replace('--', '-')

print(output)


