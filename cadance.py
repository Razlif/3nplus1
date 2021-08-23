from bitmap import BitMap

def cadance(n):
    map_string = ""
    while n != 1:
        if n%2 == 0:
            n = int(n/2)
            map_string = map_string + "0"
        else:
            n = 3*n+1
            map_string = map_string + "1"
    bm = BitMap.fromstring(map_string)
    print(bm)
    return bm

n = input("choose n: ")

cadance(int(n))
