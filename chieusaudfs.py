def DFS(graph,vertex,visited=None):
    if visited is None:
        visited=set()#gán = 1 tập hợp rỗng
    visited.add(vertex)
    print(vertex,end="-")
    for x in graph[vertex]:
        if x not in visited:
            DFS(graph,x,visited)


graph ={
    '1':['2','3'],
    '2':['4','5'],
    '3':['2','5'],
    '4':['5','6'],
    '5':['2','6'],
    '6':[]
}
print(DFS(graph,'1'))