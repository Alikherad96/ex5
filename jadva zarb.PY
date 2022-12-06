def jadval_zarb(x, y):
    chx = []
    for i in range(x):
        chy = []
        for j in range(y):
            a=(i+1)*(j+1)
            chy.append(a)
        chx.append(chy)

    for i in chx:
        for j in i:
            if j//10 == 0:
                print("   ",j,end="")
            elif j//100 == 0:
                print("  ",j,end="")
            else:
                print(" ",j,end="")
        print("")


mm = input("satr:")
nn = input("sotoon:")
m = int(mm)
n = int(nn)

jadval_zarb(m, n)



