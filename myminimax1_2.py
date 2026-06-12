import math
def minimax(scores, isMax):
    cur_lev = list(scores)
    tree_depth = int(math.log(len(cur_lev), 2))
    is_max_turn = isMax
    for depth in range(tree_depth):
        new_lev = []
        for i in range(0, len(cur_lev), 2):
            val1 = cur_lev[i]
            val2 = cur_lev[i + 1]
            
            if is_max_turn:
                res = max(val1, val2)
            else:
                res = min(val1, val2)
            new_lev.append(res)
        
        cur_lev = new_lev
        is_max_turn = not is_max_turn
    
    return cur_lev[0]

# Driver code
#oscores=[3,2,5,9]
oscores = [7, 9, 14, 21, 3, 45, 12, 8]
result = minimax(oscores, True)
print(f"The optimal value is : {result}")
