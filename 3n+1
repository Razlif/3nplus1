## create meta list of ranges

meta_list = []

## create and store a sequence based on 3n+1 in meta list

counter = 0
n = 3
while counter < 10:
    next_1 = int(n*3)
    plotted_points = []
    while n != 1:
        plotted_points.append(n)
        if (n % 2) == 0:
            n = n/2
        else:
            n = (3*n) + 1
    plotted_points.append(n)
    print("number of plotted points in this sequence: " + str(len(plotted_points)))
    meta_list.append(plotted_points)
    n = next_1
    counter += 1
print(meta_list)

## create meta list of ranges

meta_list = []

## create and store a sequence based on (n-1)/3 in meta list

counter = 0
n = 3
while counter < 1:
    plotted_points = []
    while n != 1:
        plotted_points.append(n)
        if (n % 2) == 0:
            if (n-1) % 3 == 0:
                n = (n-1)/3
                print(n)
            else:
                n = n * 2
                print(n)
        else:
            n = n * 2
            print(n)
    plotted_points.append(n)
    print("number of plotted points in this sequence: " + str(len(plotted_points)))
    meta_list.append(plotted_points)
    counter += 1
print(meta_list)

    

