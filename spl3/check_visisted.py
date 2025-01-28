from globals import visited
from visited import VISITED

def check_visited(node):
    if node not in visited:
        visited[node] = VISITED.NOT_EXPLORED
        return VISITED.NOT_EXPLORED

    return visited[node]