import numpy as np

pts = [[1,2],[2,1],[10,12],[11,10],[8,11],[14,12],[4,3]]
pts_count = len(pts)
pts = np.array(pts)
cluster1 = []
cluster2 = [i for i in range(len(pts))]
 

def CentroidLinkage(pt, cluster):
    count = 0
    total = np.array((0,0))
    for i in cluster:
        if pt != i:
            count += 1
            total += pts[i]
    # print(count, total, total/count, pts[pt])
    return np.linalg.norm(pts[pt] - total/count)


# centroid linkage
print("start", cluster2)
dists = [CentroidLinkage(i, cluster2) for i in cluster2]
index = dists.index(min(dists))
cluster2.remove(index)
cluster1.append(index)
print(dists)
print(index)
print(cluster1, cluster2)
while True:
    dists2 = [CentroidLinkage(i, cluster2) for i in cluster2]
    dists1 = [CentroidLinkage(i, cluster1) for i in cluster2]
    dists = [dists2[i] - dists1[i] for i in range(len(cluster2))]
    print(dists2)
    print(dists1)
    print(dists)
    if max(dists) < 0:
        break
    index = cluster2[dists.index(max(dists))]
    cluster2.remove(index)
    cluster1.append(index)
    print(index)
    print(cluster1, cluster2)
print("end")
print(cluster1, cluster2)
print(np.linalg.norm(\
        sum([pts[i] for i in cluster1])/len(cluster1)
        - sum([pts[i] for i in cluster2])/len(cluster2)
    ))