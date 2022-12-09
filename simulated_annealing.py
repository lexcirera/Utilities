import random
import math


def calculate_total_distance(solution):
  # Initialize the total distance
  total_distance = 0

  # Loop over the cities in the solution
  for i in range(len(solution) - 1):
    # Calculate the distance between the current city and the next city
    city1 = solution[i]
    city2 = solution[i + 1]
    distance = math.sqrt((city1[1][0] - city2[1][0])**2 + (city1[1][1] - city2[1][1])**2)

    # Add the distance to the total distance
    total_distance += distance

  # Return the total distance
  return total_distance





def simulated_annealing(cities, starting_city):
    # Initialize the temperature and the current solution
    temperature = 10000
    current_solution = [starting_city] + random.sample(cities, len(cities)) + [starting_city]

    # Initialize the best solution
    best_solution = current_solution

    # Loop until the temperature is low enough
    while temperature > 1e-8:
        # Choose two random cities
        # Choose two random cities
        city1, city2 = random.sample(range(1, len(current_solution) - 1), 2)

        # Swap the two cities in the current solution
        new_solution = current_solution[:city1] + [current_solution[city2]] + current_solution[city1 + 1:city2] + [current_solution[city1]] + current_solution[city2 + 1:]

        # Calculate the difference in total distance between the current solution and the new solution
        distance_difference = calculate_total_distance(current_solution) - calculate_total_distance(new_solution)

        # Check if the new solution is better than the current solution
        if distance_difference > 0:
        # Accept the new solution
            current_solution = new_solution

        # Update the best solution if necessary
        if calculate_total_distance(current_solution) < calculate_total_distance(best_solution):
            best_solution = current_solution
        else:
            # Calculate the probability of accepting the new solution
            probability = math.exp(distance_difference / temperature)

        # Accept the new solution with the calculated probability
        if random.random() < probability:
            current_solution = new_solution

        # Decrease the temperature
        temperature *= 0.99
        print(temperature)

    # Return the best solution
    return best_solution

# Test the simulated_annealing function
cities = [("Paris", (48.8567, 2.3508)), ("London", (51.5074, 0.1278)), ("Rome", (41.9028, 12.4964)), ("Berlin", (52.5200, 13.4050))]
starting_city = ("Paris", (48.8567, 2.3508))
print(simulated_annealing(cities, starting_city)) # [('Paris', (48.8567, 2.3508)), ('Rome', (41.9028, 12.4964)), ('London', (51.5074, 0.1278)), ('Berlin', (52.5200, 13.4050)), ('Paris', (48.8567, 2.3508))]
