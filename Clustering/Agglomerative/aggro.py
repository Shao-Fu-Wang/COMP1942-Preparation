import math

# ------------------------

SINGLE, COMPLETE, GROUPAVG, CENTROID, MEDIAN = 0, 1, 2, 3, 4
pts = [(1,2), (2,2), (5,2), (6,1)]
mode = MEDIAN

# ---------------------------

def distance(pt1, pt2):
    return ((pt1[0]-pt2[0])**2+(pt1[1]-pt2[1])**2)**0.5
class Cluster:
    def __init__(self, pt=None):
        if pt is None:
            self.pts_index = None
            self.median_mean = None
            self.centroid_mean = None
        else:
            self.pts_index = [pt]
            self.median_mean = pts[pt]
            self.centroid_mean = pts[pt]
    @staticmethod
    def merge(clus1, clus2):
        clus = Cluster()
        clus.pts_index = clus1.pts_index + clus2.pts_index
        clus.median_mean = [(clus1.median_mean[i] + clus2.median_mean[i])/2 for i in range(2)]
        clus.centroid_mean = [(clus1.centroid_mean[i]*len(clus1.pts_index) + clus2.centroid_mean[i]*len(clus2.pts_index)) /
                                (len(clus1.pts_index)+len(clus2.pts_index)) for i in range(2)]
        return clus
    @staticmethod
    def dist(clus1, clus2):
        pairwise_distances = [distance(pts[i], pts[j]) for i in clus1.pts_index for j in clus2.pts_index]
        if clus1 == clus2:
            return 0
        if mode == SINGLE:
            return min(pairwise_distances)
        elif mode == COMPLETE:
            return max(pairwise_distances)
        elif mode == GROUPAVG:
            return sum(pairwise_distances)/len(pairwise_distances)
        elif mode == CENTROID:
            return distance(clus1.centroid_mean, clus2.centroid_mean)
        elif mode == MEDIAN:
            return distance(clus1.median_mean, clus2.median_mean)
        
def aggro(clusters):
    distance_matrix = [[Cluster.dist(i, j) for j in clusters] for i in clusters]
    min_dist, clus1_index, clus2_index = float('inf'), -1, -1
    for i in range(len(clusters)):
        for j in range(len(clusters)):
            if 0.00001 < distance_matrix[i][j] < min_dist:
                min_dist, clus1_index, clus2_index = distance_matrix[i][j], i, j
    return distance_matrix, min_dist, clus1_index, clus2_index

def display_points(pts):
    return "".join(list(map(lambda x: str(x+1), pts)))

def display_matrix(distance_matrix, clusters):
    cluster_labels = [display_points(clus.pts_index) for clus in clusters]
    print(("{:<9}"*(len(clusters)+1)).format("", *cluster_labels))
    for label, row in zip(cluster_labels, distance_matrix):
        print(("{:<9}"+"{:<9.4f}"*len(clusters)).format(label, *row))

def display_cluster(cluster):
    print(cluster.pts_index, cluster.centroid_mean, cluster.median_mean)


clusters = [Cluster(i) for i in range(len(pts))]

b_i = ''
b_f = ''
distance_matrix, min_dist, clus1_index, clus2_index = aggro(clusters)
# display_matrix(distance_matrix, clusters)

for _ in range(len(pts)):
    distance_matrix, min_dist, clus1_index, clus2_index = aggro(clusters)
    if _ == len(pts) - 1:
        break
    display_matrix(distance_matrix, clusters)
    print(f'min dist = {min_dist:.4f}')
    if _ == len(pts) - 1:
        break
    new_clus = Cluster.merge(clusters[clus1_index], clusters[clus2_index])
    if mode == MEDIAN:
        print(b_i+f'new mean is {new_clus.median_mean}'+b_f)
    elif mode == CENTROID:
        print(b_i+f'new mean is {display_points(new_clus.pts_index)} is {new_clus.centroid_mean}'+b_f)
    clusters = [clusters[i] for i in range(len(clusters)) if i not in (clus1_index, clus2_index)] + [new_clus]
