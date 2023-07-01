import heapq


def dfs(graph, start, goal):
    visited = set()
    stack = [start]
    print("Start", start)
    while stack:
        node = stack.pop()
        print("Visiting", node)
        if node == goal:
            print("Reached Goal")
            return True
        if node not in visited:
            visited.add(node)
            stack.extend(graph[node])
    return False


def bfs(graph, start, goal):
    visited = set()
    queue = [start]

    while queue:
        node = queue.pop(0)

        if node == goal:
            print("Reached Goal")
            return True

        if node not in visited:
            visited.add(node)
            if node in graph:
                queue.extend(graph[node])

    return False


def greedy_search(graph, start, goal, heuristic):
    visited = set()
    # Priority queue using heuristic value as priority
    queue = [(heuristic[start], start)]
    print("Start", start)
    while queue:
        _, node = heapq.heappop(queue)
        print("Visiting", node)
        if node == goal:
            print("Reached Goal", visited)
            return True

        if node not in visited:
            visited.add(node)

            if node in graph:  # Check if node exists in the graph dictionary
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        heapq.heappush(queue, (heuristic[neighbor], neighbor))

    return False


graph = {
    "A": ["B", "D"],
    "B": ["C", "E"],
    "C": [],
    "D": ["E", "G"],
    "E": ["C", "F"],
    "F": [],
    "G": []
}

heuristic = {
    "A": 5,
    "B": 4,
    "C": 2,
    "D": 3,
    "E": 2,
    "F": 1,
    "G": 0
}

print(greedy_search(graph, "A", "G", heuristic))
# print(dfs(graph, "A", "G"))
