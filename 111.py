def two_sum(nums, target):
    # Create a dictionary to store numbers and their indices
    num_to_index = {}

    # Iterate over the list of numbers
    for index, num in enumerate(nums):
        # Calculate the complement of the current number
        complement = target - num

        # Check if the complement is already in the dictionary
        if complement in num_to_index:
            # If found, return the indices of the current number and the complement
            return [num_to_index[complement], index]

        # Store the current number and its index in the dictionary
        num_to_index[num] = index

    # If no solution is found, return None or raise an exception
    return None

# nums = [10,20,3,4,5,6, 7, 11, 15]
nums = [10,20,3,5,6,2,7, 11, 15]

target = 9
result = two_sum(nums, target)
print(result)