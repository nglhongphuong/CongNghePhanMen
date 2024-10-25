try:
    n = int(input("Nhap n: "))
except ValueError as ex:
    print(str(ex))
else:
    for i in range (n):
        print(' '*(n-i) + '*'*i)

    for i in range(n):
        print(i*'*' + (n-i) * ' ')

    for i in range(n):
        print(n*'*')