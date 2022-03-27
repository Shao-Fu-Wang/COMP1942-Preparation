import math

a = [[1, 2], [2, 2], [5, 2], [6, 1]]

for k in range(1):
    print(end="\t\t")
    for i in range(len(a)):
        print("cluster",i+1, end='\t')
    print()
    d = []
    new_set_point = [0, 0]
    min = 9999999
    min_idx = -1
    min_x = -1
    min_y = -1
    min_smaller = -1
    for i in range(len(a)): 
        for j in range(len(a)): 
            d.append(round((math.sqrt((a[i][0]-a[j][0])**2 + (a[i][1]-a[j][1])**2)), 3))
    for i in range(len(d)):
        if d[i] < min and d[i] > 0:
            min = d[i]
            min_idx = i
    min_x = min_idx % len(a)
    min_y = math.floor(min_idx/len(a))
    new_set_point[0] = (a[min_x][0]+a[min_y][0])/2
    new_set_point[1] = (a[min_x][1]+a[min_y][1])/2
    if(min_x <= min_y):
        min_smaller = min_x
        min_bigger = min_y
    else:
        min_smaller = min_y
        min_bigger = min_x
    for i in range(len(d)):
        if(i%len(a) == 0):
            print('cluster', math.floor(i/len(a))+1, end = '\t')
        print(d[i], end = 2*'\t')
        if((i+1)%len(a) == 0):
            print()

    # print("merge cluster"+str(min_x+1), "and cluster"+str(min_y+1), "because distance is smallest:", min)
    a[min_smaller] = new_set_point
    a.pop(min_bigger)
    # print("min_smaller =",min_smaller)
    # print("min_bigger =",min_bigger)
    # print(new_set_point)
    # print("new cluster midpoint: "+str(new_set_point)+"\n")
