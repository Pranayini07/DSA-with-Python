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
    def dfs(self,start):
        stack = [start]
        visited = []
        while stack:
            temp = stack.pop() # s
            if temp not in visited:
                stack.extend(self.graph[temp])
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
obj.dfs("s")