class graph:
    def __init__(self,size):
        self.adjmatrix = [[0]*size for i in range(size)]
        self.vertexdata = ['']*size
        self.size = size

    def addedge(self,u,v,weight):
        if 0 <= u < self.size and 0 <= v <self.size:
            self.adjmatrix[u][v] = weight
            self.adjmatrix[v][u] = weight

    def addvertxdata(self, vertex, data):
        if 0<= vertex <self.size:
            self.vertexdata[vertex] = data


    def dijkstra(self,startvertexdata):
        startvertex = self.vertexdata.index(startvertexdata)
        distance = [float('inf')] * self.size
        distance[startvertex] =0
        visited = [False]*self.size


        for _ in range (self.size):
            mindistance = float('inf')
            u = None
            for i in range(self.size):
                if not visited[i] and distance[i] < mindistance:
                    mindistance = distance[i]
                    u = i 

            if u is None:
                break

            visited[u] = True

            for v in range(self.size):
                if self.adjmatrix[u][v] != 0 and not visited[v]:
                    alt = distance[u] + self.adjmatrix[u][v]
                    if alt < distance[v]:
                        distance[v] = alt
        return distance

g= graph(5)

g.addvertxdata(0,"A")
g.addvertxdata(1,"B")
g.addvertxdata(2,"C")
g.addvertxdata(3,"D")
g.addvertxdata(4,"E")

g.addedge(3,1,3)
g.addedge(3,2,4)
g.addedge(3,4,7)
g.addedge(3,1,3)


g.addedge(0,1,3)
g.addedge(0,2,1)
g.addedge(0,3,14)
g.addedge(0,4,7)



g.addedge(1,2,13)
g.addedge(1,4,14)
g.addedge(2,4,9)


distances = g.dijkstra("D")

for i,d in enumerate(distances):
    print(g.vertexdata[i], d)