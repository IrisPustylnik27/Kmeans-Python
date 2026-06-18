


class Cluster(object):

    def __init__(self, centroid):
        self.centroid = centroid
        self.points = []

    def update_centoroid(self):
        if not self.points:
            return
        sum = vector([0] * len(self.points[0]))
        for point in self.points:
            sum += point
        self.centoroid = sum / len(self.points)

class vector(object):

    def __init__(self, values):
        self.values = values

    def __add__(self, other):
        return vector([a + b for a, b in zip(self.values, other.values)])

    def __truediv__(self, scalar):
        return vector([a / scalar for a in self.values])
    



    