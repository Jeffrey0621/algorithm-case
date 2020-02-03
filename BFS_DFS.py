from queue import Queue
def bfs(node,start):
    visited = set()
    q = Queue()
    q.put(start)
    while not q.empty():
        u = q.get()
        print(u)
        for v in node.get(u,[]):
            if v not in visited:
                visited.add(v)
                q.put(v)

def dfs(node,start):
    visited = set()
    stack = [[start,0]]
    while stack:
        (v,next_child_idx) = stack[-1]
        if (v not in node) or (next_child_idx >= len(node[v])):
            stack.pop()
            continue
        next_child = node[v][next_child_idx]
        stack[-1][1] += 1
        if next_child in visited:
            continue
        print(next_child)
        visited.add(next_child)
        stack.append([next_child,0])
        

graph = {1: [4, 2], 2: [3, 4], 3: [4], 4: [5]}
bfs(graph, 1)
dfs(graph,1)
