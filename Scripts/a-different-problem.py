while True:
    try:
        a = input().split()
        a = int(a[0]) - int(a[1])
        a = abs(a)
        print(a)
    except EOFError:
        break


