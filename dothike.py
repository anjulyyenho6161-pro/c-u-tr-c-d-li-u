from collections import deque
def bfs(graph,start):
     queue=deque([start])
     visited = set([start])
     while queue:
         vertex=queue.popleft()
         print(vertex,end=" ")
         for neighbor in graph[vertex]:
             if neighbor not in visited:
                 queue.append(neighbor)
                 visited.add(neighbor)


graph={
    'A':['C','D','E'],
    'B':['C','E'],
    'C':['A','B','E','F','G'],
    'D':['A'],
    'E':['A','C'],
    'F':['B'],
    'G':['C']
}
print("kết quả duyệt đồ thị theo chiều rộng")
bfs(graph,'D')
