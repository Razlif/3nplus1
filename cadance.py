def cadance(n):
    bmap = []
    while n != 1:
        if n%2 == 0:
            n = int(n/2)
            bmap.append("0")
        else:
            n = 3*n+1
            bmap.append("1")
    print(bmap)

n = input("choose n: ")

cadance(int(n))
