def binary_search(sorted_list, value):
  # Set the initial bounds of the search
  lower_bound = 0
  upper_bound = len(sorted_list) - 1

  # Keep searching until the bounds meet or the value is found
  while lower_bound <= upper_bound:
    # Calculate the middle index of the current search bounds
    mid = (lower_bound + upper_bound) // 2

    # Check the value at the middle index
    if sorted_list[mid] == value:
      # Return the index if the value is found
      return mid
    elif sorted_list[mid] < value:
      # Search the upper half of the list if the value is greater than the middle value
      lower_bound = mid + 1
    else:
        # Search the lower half of the list if the value is less than the middle value
        upper_bound = mid - 1

  # Return None if the value is not found in the list
  return None

# Test the binary_search function
sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(binary_search(sorted_list, 7)) # 6
print(binary_search(sorted_list, 69)) # None
