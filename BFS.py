class Graph:
    def __init__(self):
        self.graph ={}  # s : [sa]
    def insert(self,u,v):
        for j in range(2):
            if u not in self.graph:
                self.graph[u] = [v]
            else:
                self.graph[u].append(v)
            u , v  = v,u
    def bfs(self,start):
        queue = [start]
        visited = []
        while queue:
            temp = queue.pop(0) # s
            if temp not in visited:
                queue.extend(self.graph[temp])
                visited.append(temp)
        print(visited)



obj = Graph()
obj.insert("s","sa")
obj.insert("s","r")
obj.insert("s","p")
obj.insert("s","k")
obj.insert("sa","k")
obj.insert("r","v")
obj.insert("sa","p")
print(obj.graph)
obj.bfs("s")