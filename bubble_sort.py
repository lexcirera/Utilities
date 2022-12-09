def bubble_sort(numbers):
  # Keep looping until the list is fully sorted
  while True:
    # Assume the list is already sorted
    is_sorted = True

    # Loop over the list and compare adjacent elements
    for i in range(len(numbers) - 1):
      if numbers[i] > numbers[i + 1]:
        # Swap the elements if they are in the wrong order
        numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
        is_sorted = False

    # If no swaps were made, the list is already sorted
    if is_sorted:
      break

# Test the bubble_sort function
numbers = [5, 2, 1, 4, 3]
print("List to sort: ", numbers)
bubble_sort(numbers)
print("Sorted list: ", numbers) # [1, 2, 3, 4, 5]
