arr = [int(x) for x in input("Enter the elements of the array separated by spaces: ").split()]
arr.sort()  

target = int(input("Enter the target element to search for: ")) 

print("Sorted array:", arr)


start = 0
end = len(arr) - 1
found = False

while start <= end:
    mid = (start + end) // 2

    if arr[mid] == target:
        print("Element found at index:", mid)
        found = True
        break
    elif arr[mid] < target:
        start = mid + 1
    else:
        end = mid - 1

if not found:
    print("Element not found")