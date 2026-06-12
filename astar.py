def astar(graph, start, goal):
    pq = [[0,0,0,start]] # a queue which store [f,h,g,node] as single unit
    visited = []
    while pq:
        f,h,g,cnode = pq.pop(0)
        visited.append([f,h,g,cnode])
        for neigh, wt in graph[cnode[-1]].items(): #wt[0] has g, wt1 has h
            g1=g+wt[0]
            f1=g1+wt[1]
            path=cnode+neigh
            pq.append([f1,wt[1],g1,path])
            pq=sorted(pq)
    
    visitedf=[]
    for x in visited:
        if x[3].endswith(goal):
            visitedf.append(x)
    print(visited)  
    print("~~~~~~~~~~~~~~~~~~~~~~~")    
    
    return sorted(visitedf)

# graph = {
#     'A': {'B': [2,3], 'C': [1,6]},
#     'B': {'D': [4,0]},
#     'C': {'D': [7,0]},
#     'D': {}
# }

graph = {
     'A': {'B': [3,8], 'C': [2,9]},
     'B': {'D': [3,7], 'E': [4,6]},
     'C': {'F': [5,4]},
     'D': {'G': [6,0]},
     'E': {'G': [9,0]},
     'F': {'G': [6,0]},
     'G': {}
}
start = 'A'
goal = 'G'
visitedf=(astar(graph, start, goal))
print("The shortest Path is ",visitedf[0][-1]," with a cost of ",visitedf[0][-2]," Units")
