def mergesort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        lefthalf = arr[:mid]
        righthalf = arr[mid:]

        # Recursively sort the two halves
        mergesort(lefthalf)
        mergesort(righthalf)

        i = j = k = 0

        # Merge the sorted halves
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                arr[k] = lefthalf[i]
                i += 1
            else:
                arr[k] = righthalf[j]
                j += 1
            k += 1

        # Check if any element was left in the lefthalf
        while i < len(lefthalf):
            arr[k] = lefthalf[i]
            i += 1
            k += 1

        # Check if any element was left in the righthalf
        while j < len(righthalf):
            arr[k] = righthalf[j]
            j += 1
            k += 1

# Example usage:
arr = [12, 11, 13, 5, 6, 7]
mergesort(arr)
print("Sorted array is:", arr)
