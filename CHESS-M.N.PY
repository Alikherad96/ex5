
mm = input("tedade satr ha =")
nn = input("tedade sotoon ha =")
m = int(mm)
n = int(nn)


def chess(m, n):
    chm = []
    for i in range(m):
        chn = []
        for j in range(n):
            if (i + j) % 2 == 0:
                chn.append("#")
            else:
                chn.append("*")
            #print(i,j)
        chm.append(chn)
    #print(chm)

    for i in chm:
        for j in i:
            print(j, end="")
        print("")


chess(m, n)


