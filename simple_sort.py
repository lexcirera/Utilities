# Define the sorting algorithm
def sort(arr):
  # Iterate over the array, starting at the second element
  for i in range(1, len(arr)):
    # Store the current element in a temporary variable
    current = arr[i]
    # Store the index of the previous element
    j = i - 1
    # Move the previous element to the right until it is in the correct position
    while j >= 0 and arr[j] > current:
      arr[j+1] = arr[j]
      j -= 1
    # Insert the current element in the correct position
    arr[j+1] = current
  # Return the sorted array
  return arr

# Test the sorting algorithm
arr = [5, 2, 4, 6, 1, 3]
print(sort(arr)) # [1, 2, 3, 4, 5, 6]
