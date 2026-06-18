import sys


class Cluster(object):

    def __init__(self, centroid):
        self.centroid = centroid
        self.points = []

    def update_centoroid(self):
        if not self.points:
            return
        sum = Vector([0] * len(self.points[0]))
        for point in self.points:
            sum += point
        self.centoroid = sum / len(self.points)

class Vector(object):

    def __init__(self, values):
        self.values = values

    def __add__(self, other):
        return vector([a + b for a, b in zip(self.values, other.values)])

    def __truediv__(self, scalar):
        return vector([a / scalar for a in self.values])
    
def main():
    epsilon = 0.001
    deltaCentroid = 0.0
    d, N, k, iter, counter = 0, 0, 0, 400, 0
    isConverged = False
    fileName = ""
    clusters, vectors = [], []

    # taking args
    if len(sys.argv) < 2:
        print("not enough arguments")
        sys.exit(1)  

    if len(sys.argv) > 4:
        print("too many arguments")
        sys.exit(1)

    if len(sys.argv) == 3:
        filename = sys.argv[2]
    
    if len(sys.argv) == 4:
        iter = int(sys.argv[2])
        filename = sys.argv[3]
    

    # read data from file
    try:
        with open(filename, 'r') as f:
            for line in f:
                vector = Vector([float(val) for val in line.strip().split(',')])
                vectors.append(vector)
                N += 1
                if d == 0:
                    d = len(vector.values)
    except FileNotFoundError:
        print(f"File {filename} not found.")
        sys.exit(1)
    
    # Initialize centroids 
    for i in range(k):
        centroid = Vector(vectors[i].values)
        clusters.append(Cluster(centroid))
    
    while not isConverged and iter > counter:
        # Assign points to clusters
        isConverged = True
        for vector in vectors:
            closest_cluster = min(clusters, key=lambda c: euclidean_distance(vector, c.centroid))
            closest_cluster.points.append(vector)
            centroid = closest_cluster.centroid
            closest_cluster.update_centoroid()
            deltaCentroid = euclidean_distance(centroid, closest_cluster.centroid)
            if (deltaCentroid >= epsilon):
                isConverged = False
        counter += 1
    
    printCenteroids(clusters)

    
def printCenteroids(clusters):
    for i, cluster in enumerate(clusters):
        print(f"{cluster.centroid.values}\n")
    

def euclidean_distance(vec1, vec2):
    return sum((a - b) ** 2 for a, b in zip(vec1.values, vec2.values)) ** 0.5


    