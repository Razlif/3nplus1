# update the list of hailstone numbers of a given number n
def update(n, l):
    while n != 1:
        l.append(n)
        if n%2 == 0:
            n = int(n/2)
        else:
            n = 3*n+1
    l.append(1)

##################################################
# recursive implementations of the above functions
##################################################

# update the list of hailstone numbers of a given number n
def update_rec(n, l):
    l.append(n)
    if n == 1:
        return
    if n%2 == 0:
        calculate_list(int(n/2), l)
    else:
        calculate_list(3*n+1, l)

