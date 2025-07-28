def linear_search(arr,key):
    for i in range(len(arr)):
        if key==arr[i]:
            return f"value found in the index of {i}"
    return "not found"
a = [10,4,7,9,16,6]
print(linear_search(a,10))