"""
Two sum task from leetcode, see README.md for details

Date: 5th of May 2022
Author: Nadejda Jaeverberg
"""


def two_sum(nums, target):
    """
    Return indices for the elements in the input list nums that add up to target
    :param nums: list of integers
    :param target: an integer
    :return:
    """
    # Check the input in case of issues:
    if not isinstance(target, int):
        print(f"Target is not an integer! Provided target value is: {target} with type: {type(target)}")
        return None

    check_list = [elem for elem in nums if not isinstance(elem, int)]

    if len(check_list) > 0:
        print(f"The provided list is not a list of integers only. Provided list: {nums}, "
              f"non-integer elements found: {check_list}")
        return None

    # Since there can only be one solution, it is possible to stop as soon as it is found.
    # There is no need to loop through the entire list
    for i in range(len(nums)):
        # Take ith element on the list
        one_num = nums[i]
        # Make a subset of the list of all the elements that come after the ith element
        cut_nums = nums[i+1:]
        # Loop through the shorter list
        for j in range(len(cut_nums)):
            # Check if the sum equals the target
            if one_num + cut_nums[j] == target:
                print(f"Found number {one_num} with index {i} and number {cut_nums[j]} with index {i+j+1}")
                # Return the answer
                return [i, i + j + 1]
    # If after looping and checking all elements the answer isn't found then return None
    print("Failed to find elements in the list to add up to target.")
    return None


if __name__ == "__main__":
    list_in1 = [2, 7, 11, 15]
    target1 = 9

    summed_output = two_sum(list_in1, target1)

    print(f"Indices from the list: {list_in1} for elements adding up to {target1} will be: {summed_output}")
