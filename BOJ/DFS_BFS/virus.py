def DFS(graph,root,visited=[]):
    visited.append(root)
    for node in graph[root]:
        if node not in visited:
            DFS(graph,node,visited)
    return visited

N = int(input())
V = int(input())

graph = [[] for x in range(N+1)]

while V > 0:
    start, end = map(int,input().split())
    graph[start].append(end)
    graph[end].append(start)
    V -= 1

result = DFS(graph,1)
print(len(result)-1)