# Ford-Fulkerson algorithm
# This code fails 2 test cases out of 10.

class Edge(object):
    def __init__(self, u, v, w):
        self.source = u
        self.target = v
        self.capacity = w

    def __repr__(self):
        return "%s->%s:%s" % (self.source, self.target, self.capacity)


class FlowNetwork(object):
    def  __init__(self):
        self.adj = {}
        self.flow = {}

    def AddVertex(self, vertex):
        self.adj[vertex] = []

    def GetEdges(self, v):
        return self.adj[v]

    def AddEdge(self, u, v, w = 0):
        if u == v:
            raise ValueError("u == v")
        edge = Edge(u, v, w)
        redge = Edge(v, u, 0)
        edge.redge = redge
        redge.redge = edge
        self.adj[u].append(edge)
        self.adj[v].append(redge)
        # Intialize all flows to zero
        self.flow[edge] = 0
        self.flow[redge] = 0

    def FindPath(self, source, target, path):
        if source == target:
            return path
        for edge in self.GetEdges(source):
            residual = edge.capacity - self.flow[edge]
            if residual > 0 and not (edge, residual) in path:
                result = self.FindPath(edge.target, target, path + [(edge, residual)])
                if result != None:
                    return result

    def MaxFlow(self, source, target):
        path = self.FindPath(source, target, [])
        while path != None:
            flow = min(res for edge, res in path)
            for edge, res in path:
                self.flow[edge] += flow
                self.flow[edge.redge] -= flow
            path = self.FindPath(source, target, [])
        return sum(self.flow[edge] for edge in self.GetEdges(source))


g = FlowNetwork()

t = int(raw_input())
n, m = map(int, raw_input().split())
map(g.AddVertex, range(m+1))

for _ in range(t-1):
    inp = map(int, raw_input().split())
    #print inp
    g.AddEdge(inp[0], inp[1], inp[2])


print g.MaxFlow(0, m)
