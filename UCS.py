#updated UCS (cumulative cost)
def ucs(graph, start, goal):
    pq = [[0,start]]
    visited = []
    while pq:
        g,cnode = pq.pop(0)
        visited.append([g,cnode])
        #print("visited ",visited)
        if cnode[-1]==goal:
            return visited[-1]
        
        for neigh, wt in graph[cnode[-1]].items(): 
            g1=g+wt
            path=cnode+neigh
            pq.append([g1,path])
            pq=sorted(pq)
    
graph = {
     'A': {'B': 3, 'C': 2},
     'B': {'D': 4, 'E': 5},
     'C': {'F': 10},
     'D': {'G': 3},
     'E': {'G': 1},
     'F': {'G': 1},
     'G': {}
}
start = 'A'
goal = 'G'

visitedf=(ucs(graph, start, goal))
print("The shortest Path is ",visitedf)

