import heapq

def a_star_search(graph, start, goal, heuristic):
    open_list = [(0, start)]  # Priority queue with f-score and node
    closed_list = set()
    g_scores = {node: float('inf') for node in graph}
    g_scores[start] = 0
    parents = {}

    while open_list:
        _, current_node = heapq.heappop(open_list)

        if current_node == goal:
            return reconstruct_path(parents, start, goal)

        closed_list.add(current_node)

        if current_node in graph:
            for neighbor, edge_cost in graph[current_node].items():
                if neighbor in closed_list:
                    continue

                new_g_score = g_scores[current_node] + edge_cost

                if new_g_score < g_scores[neighbor] or neighbor not in [node for _, node in open_list]:
                    g_scores[neighbor] = new_g_score
                    parents[neighbor] = current_node
                    f_score = new_g_score + heuristic[neighbor]
                    heapq.heappush(open_list, (f_score, neighbor))

    return None

def reconstruct_path(parents, start, goal):
    path = [goal]
    current_node = goal

    while current_node != start:
        current_node = parents[current_node]
        path.append(current_node)

    path.reverse()
    return path

# Example usage:
graph = {
    'Arad': {'Zerind': 75, 'Timisoara': 118, 'Sibiu': 140},
    'Zerind': {'Arad': 75, 'Oradea': 71},
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
    'Mehadia': {'Lugoj': 70, 'Drobeta': 75},
    'Drobeta': {'Mehadia': 75, 'Craiova': 120},
    'Craiova': {'Drobeta': 120, 'Rimnicu': 146, 'Pitesti': 138},
    'Rimnicu': {'Craiova': 146, 'Sibiu': 80, 'Pitesti': 97},
    'Sibiu': {'Arad': 140, 'Oradea': 151, 'Rimnicu': 80, 'Fagaras': 99},
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Pitesti': {'Rimnicu': 97, 'Craiova': 138, 'Bucharest': 101},
    'Bucharest': {'Fagaras': 211, 'Pitesti': 101, 'Giurgiu': 90, 'Urziceni': 85},
    'Giurgiu': {'Bucharest': 77},
    'Urziceni': {'Bucharest': 85, 'Hirsova': 98, 'Vaslui': 142},
    'Hirsova': {'Urziceni': 98, 'Eforie': 86},
    'Eforie': {'Hirsova': 86},
    'Vaslui': {'Urziceni': 142, 'Iasi': 92},
    'Iasi': {'Vaslui': 92, 'Neamt': 87},
    'Neamt': {'Iasi': 87}
}

heuristic = {
    'Arad': 366,
    'Bucharest': 0,
    'Craiova': 160,
    'Drobeta': 242,
    'Eforie': 161,
    'Fagaras': 178,
    'Giurgiu': 90,
    'Hirsova': 151,
    'Iasi': 226,
    'Lugoj': 244,
    'Mehadia': 241,
    'Neamt': 234,
    'Oradea': 380,
    'Pitesti': 98,
    'Rimnicu': 193,
    'Sibiu': 253,
    'Timisoara': 329,
    'Urziceni': 80,
    'Vaslui': 199,
    'Zerind': 374
}

start_node = 'Arad'
goal_node = 'Bucharest'

shortest_path = a_star_search(graph, start_node, goal_node, heuristic)
if shortest_path:
    print("Shortest path:", shortest_path)
else:
    print("No path found from", start_node, "to", goal_node)
