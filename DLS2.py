#DLS Complete
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

def My_DLS(graph, start, goal, L):
    stack = [(start, 0)]
    while stack:
        node, depth = stack.pop(0)
        if node == goal:
            return True, goal, depth
        if depth < L:
            for n in graph[node]:
                stack.insert(0,(n, depth + 1))
    return False, goal, -1

#############
L = 3 #depth limit
n,g,d = My_DLS(graph, '6', '5', L)
if n:
    print("Goal ",g," found at level ",d)
else:
    print("Goal ",g," not found ",d)
