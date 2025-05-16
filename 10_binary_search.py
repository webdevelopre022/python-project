# binary_search.py
#YouTube channel 5starcoder
#subscribe my channel 
#project_10

def binary_search(arr, target):
    """
    Perform binary search on a sorted array.

    Parameters:
    arr (list): The sorted list to search.
    target (any): The value to search for.

    Returns:
    int: The index of target in arr if found, else -1.
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

if __name__ == "__main__":
    # Example usage
    arr = [1, 3, 5, 7, 9, 11, 13]
    target = int(input("Enter the number to search: "))

    result = binary_search(arr, target)
    if result != -1:
        print(f"Element found at index {result}")
    else:
        print("Element not found")
