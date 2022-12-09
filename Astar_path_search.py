'''
A* search algorithm to find the shortest path between two nodes in a graph
'''


import heapq

def a_star(graph, start, goal):
  # Initialize the priority queue and explored set
  queue = []
  heapq.heappush(queue, (0, start))
  explored = set()

  # Initialize the distances and parents dictionaries
  distances = {start: 0}
  parents = {start: None}

  # Loop until the queue is empty or the goal is reached
  while queue:
    # Pop the node with the lowest total cost from the queue
    current = heapq.heappop(queue)[1]


    # Check if the goal has been reached
    if current == goal:
        # Create the path by following the parents back from the goal node
        path = [goal]
        while parents[path[-1]] is not None:
            path.append(parents[path[-1]])
        path.reverse()

    # Return the path and the distances dictionary
        return path, distances

    # Loop over the neighbors of the current node
    for neighbor in graph[current]:
    # Calculate the actual cost to the neighbor
        cost = distances[current] + graph[current][neighbor]

    # Check if the neighbor has not been explored or if the cost is lower than the previously recorded distance
    if neighbor not in distances or cost < distances[neighbor]:
        # Update the distances and parents dictionaries
        distances[neighbor] = cost
        parents[neighbor] = current

        # Calculate the estimated total cost to the goal
        heuristic = abs(goal[0] - neighbor[0]) + abs(goal[1] - neighbor[1])
        priority = cost + heuristic

        # Push the neighbor into the priority queue
        heapq.heappush(queue, (priority, neighbor))

        # Return None if the goal is not reached
        return None

# Test the a_star function
graph = {(0, 0): {(1, 0): 1, (0, 1): 1}, (1, 0): {(0, 0): 1, (1, 1): 1}, (0, 1): {(0, 0): 1, (1, 1): 1}, (1, 1): {(1, 0): 1, (0, 1): 1}}
print(a_star(graph, (0, 0), (1, 1))) # ([(0, 0), (1, 0),(1,1)]O)
