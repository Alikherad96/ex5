def khayam(n):
    khj = []
    khjj =[]
    for j in range(n):
        khi = []
        for i in range(n):
            if i == 0:
                khi.append(1)
            else:
                khi.append(0)
        khj.append(khi)
        khjj.append(khi)
    khj[1][1] = 1

    for j in range(1, n):
        for i in range(1, j+1):
            khj[j][i] = int(khj[j-1][i])+int(khj[j-1][i-1])
    k1=k2=0
    for i in range(n):
        for j in range(n):
            if khj[j][i]==0:
                khj[j][i]=""
                #print("555")
            khjj[j][i]=str(khj[j][i])
            k1=len(khjj[j][i])
            #print(k1)
            if k1>k2:
                k2=k1
            #fahmidane bozrg tarin toole araye

    for i in khj:
        for j in i:
            jj=str(j)
            for k in range(k2-len(jj)):
                #gozashtane jaye khali baraye zire ham gharar gereftane adad
                print(" ", end="")
            print("  ",j,end="")
        print("")


nn = input("how many rows do u like in khayam_paskal mosalas , dont woory , we have estimated every thing  = ?")
n = int(nn)
khayam(n)