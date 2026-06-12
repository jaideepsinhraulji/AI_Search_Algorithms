#UCS with incurring cumulative weights
from queue import PriorityQueue
graph = {
    'A': {'B': 2, 'C': 1},
    'B': {'D': 3, 'E': 4},
    'C': {'F': 5},
    'D': {'G': 6},
    'E': {'G': 7},
    'F': {'G': 8},
    'G': {}
}
# graph = {
#     'A': {'B': 2, 'C': 1},
#     'B': {'D': 4},
#     'C': {'D': 3},
#     'D': {}
# }

visitedpq = PriorityQueue() # List for visited nodes.

def ucs(graph, node, goal): #function for BFS
  pq=PriorityQueue()  #Initialize a queue  
  pq.put([0,node])
  visitedpq.put([0,node])
  tn='x'
  tw=0
  while not pq.empty():#empty returns true if empty     
    tw,tn=pq.get()
    visitedpq.put([tw,tn])
    if tn==goal:
        break
    else:
        for neigh,weight in graph[tn].items():  
            pq.put([weight+tw,neigh])
        #visited.append(tn)
        
# Driver Code
print("Following is the UCS")
ucs(graph, 'A','D')    # A is start state and G is a goal node
while not visitedpq.empty():
    tw,tn = visitedpq.get()
    if(tn=='D'):
        print(tn)
        break
    print(tn)
