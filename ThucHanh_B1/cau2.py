try:
    n = int(input("Nhap n: "))
except ValueError as ex:
    print(str(ex))
else:
    a = [] #list
    # for i in range(n):
    #     a.append(int(input(f"a[{i}] = ")))
    a = [int(input(f"a[{i} = ")) for i in range(n)]

    d = [x for x in a if x > 0]
    print(max(d) if len(d) > 0 else '*')

    e = [x for x in a if x < 0]
    print(min(e) if len(e) > 0 else '*')
    # if max(a) > 0:
    #     print(f"So duong lon nhat: {max(a)}")
    # else:
    #     print("So duong lon nhat: *")
    #
    # if min(a) < 0:
    #     print(f"So am be nhat: {min(a)}")
    # else:
    #     print("So am  be nhat: *")

    a.sort(reverse=True)
    print(a)
    #Hiển thị tần số xuất hiện của từng phần tử trong danh sác
    for i in set(a):
        print(f"{i} xuat hien {a.count(i)} lan")

