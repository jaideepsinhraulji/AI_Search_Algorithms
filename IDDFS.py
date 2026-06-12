#Iterative Deepening Depth First Search
graph = {
    '6': ['4', '8'],
    '4': ['3', '5'],
    '8': ['9'],
    '3': ['10'],
    '5': ['11'],
    '9': ['12'],
    '10': [],
    '11': [],
    '12': []
}

def My_DLS(graph, start, goal, limit):
    stack = [(start, 0)]
    while stack:
        node, depth = stack.pop()
        if node == goal:
            return True, goal, depth
        if depth < limit:
            for n in graph[node]:
                stack.insert(0,(n, depth + 1))
    return False, goal, -1

#############
limit = 3 #depth limit
i=0
while(i<limit): #IDDFS / DLS XXwhile
       #def My_DLS(graph, start, goal, limit):
    b,g,d = My_DLS(graph, '6', '11', limit)
    if b:
        print("Goal ",g," found at level ",d)
        break
    else:
        print("Goal ",g," not found ",d)
    i=i+1
