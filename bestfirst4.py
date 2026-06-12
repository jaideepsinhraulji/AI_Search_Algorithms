#Best First Search - Complete
graph = {
    'A': {'B': 12, 'C': 11},
    'B': {'D': 9, 'E': 10},
    'C': {'F': 6, 'G': 7},
    'D': {'H': 0},
    'E': {'H': 0},
    'F': {'H': 0},
    'G': {'H': 0},
    'H': {}
}

def bestFirstSearch(graph, start, goal):
    pq = [[0, start]]
    visited = []
    while pq:
        pq.sort()        
        cw, cn = pq.pop(0)        
        if cn not in visited:
            visited.append(cn)
            if cn == goal:
                break            
            for n, wt in graph[cn].items():
               pq.append([wt, n])
    
    print("Visited Path:", visited)

# Driver Code
print("Best First Search :")
bestFirstSearch(graph, 'A', 'H')