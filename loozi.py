def loozi(n):
    lj = []
    #nimeye balaye loozi
    for j in range(n):
        li = []
        k = (2 * n - 1) - (2 * j + 1)
        for i in range(k // 2):
            li.append(" ")
        for i in range(2 * j + 1):
            li.append("*")
        for i in range(k // 2):
            li.append(" ")
        lj.append(li)

    #nimeye payine loozi
    j = n-1
    while j > 0:
        j = j-1
        li = []
        k = (2 * n - 1) - (2 * j + 1)
        for i in range(int(k/2)):
            li.append(" ")
        for i in range(2*j+1):
            li.append("*")
        for i in range(int(k/2)):
            li.append(" ")
        lj.append(li)

    for i in lj:
        for j in i:
            print(j, end="")
        print("")


aa = input("tedade loozi ha = ?")
a = int(aa)
loozi(a)
