def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

print(linear_search([10, 20, 30, 40, 50], 30))
print(linear_search([1, 5, 9, 3, 7], 8))
print(linear_search([15, 25, 35, 45], 25))
