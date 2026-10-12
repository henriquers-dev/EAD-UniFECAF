from collections import deque

def bfs(graph, start, goal):
    visited = set()
    queue = deque([start])

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == go:
            return path
        
        if node not in visited:
            visited.add(node)
            for neighbor in graph.get(node, []):
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
    
    return None


# Exemplo de uso:
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print(bfs(graph, 'A', 'F'))  # Saída: ['A', 'C', 'F'] ou ['A', 'B', 'E', 'F']
