from typing import List


# Write any import statements here

def getHitProbability(R: int, C: int, G: List[List[int]]) -> float:
    # Write your code here
    result: float
    total_amount_of_cells = R*C
    total_amount_of_ships = 0
    for r in range(min(R,len(G))):
        for c in range(min(C,len(G[0]))):
            if G[r][c] == 1:
                total_amount_of_ships += 1
    result = total_amount_of_ships / total_amount_of_cells
    return result


print(getHitProbability(3, 3, [[0, 0, 0], [0, 0, 0],[1, 1, 1]]))
