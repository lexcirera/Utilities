def quick_sort(numbers):
  # Return the list if it has 0 or 1 elements
  if len(numbers) <= 1:
    return numbers

  # Select the pivot value as the middle element of the list
  pivot = numbers[len(numbers) // 2]

  # Initialize the left and right partitions
  left = []
  right = []

  # Loop over the numbers and partition them based on the pivot
  for number in numbers:
    if number < pivot:
      left.append(number)
    elif number > pivot:
      right.append(number)

  # Recursively quick sort the left and right partitions
  left = quick_sort(left)
  right = quick_sort(right)

  # Concatenate the left, pivot, and right partitions and return the result
  return left + [pivot] + right

# Test the quick_sort function
numbers = [5, 2, 1, 4, 3]
print("List to sort: ", numbers)
bubble_sort(numbers)
print("Sorted list: ", numbers) # [1, 2, 3, 4, 5]
