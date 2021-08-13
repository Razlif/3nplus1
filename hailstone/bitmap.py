# generate a bitmap with ther hailstone numbers of a given number n
def generate(n, max_number):
    m = [0 for i in range(max_number)]
    m[1] = 1
    while n != 1:
        if n >= len(m):
            print(str(n) + " is out of map range")
            break
        if m[n] == 1:
            # no need to continue we reached a value
            # already in the map
            break

        m[n] = 1
    
        if n%2 == 0:
            n = int(n/2)
        else:
            n = 3*n+1
    return m

# update a bitmap with ther hailstone numbers of a given number n
def update(n, m):
    while n != 1:
        if n >= len(m):
            print(str(n) + " is out of map range")
            break
        if m[n] == 1:
            # no need to continue we reached a value
            # already in the map
            break

        m[n] = 1
    
        if n%2 == 0:
            n = int(n/2)
        else:
            n = 3*n+1

    m[1] = 1

# print the hailstone numbers in the bitmap
def print_map(m):
    for i in range(len(m)):
        if m[i] == 1:
            print(i)

##########################
# recursive implementation
##########################

# updating a bitmap with ther hailstone numbers of a given number n
def update_rec(n, m):
    if n >= len(m):
        print(str(n) + " is out of map range")
        return

    if m[n] == 1:
        # no need to continue we reached a value
        # already in the map
        return

    m[n] = 1
    
    if n == 1:
        return

    if n%2 == 0:
        update_map(int(n/2), m)
    else:
        update_map(3*n+1, m)

# generate a bitmap with ther hailstone numbers of a given number n
def generate_rec(n, max_number):
    m =  [0 for i in range(max_number)]
    update_map_rec(n, m)
    return m

