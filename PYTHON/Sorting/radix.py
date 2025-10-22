def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10  # for digits 0–9

    # Count occurrences of digits
    for num in arr:
        index = (num // exp) % 10
        count[index] += 1

    # Convert count[i] to position indexes
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build output (stable sort)
    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    # Copy to arr
    for i in range(n):
        arr[i] = output[i]


def radix_sort(arr):
    if not arr:
        return

    max_val = max(arr)

    exp = 1
    while max_val // exp > 0:
        counting_sort(arr, exp)
        exp *= 10


# Example usage
if __name__ == "__main__":
    arr = [170, 45, 75, 90, 802, 24, 2, 66]
    print("Original array:", arr)
    radix_sort(arr)
    print("Sorted array:  ", arr)
