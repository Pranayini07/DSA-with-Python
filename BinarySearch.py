def Binary_search(key):
    s = 0
    e = len(a)-1
    while s<=e:
        mid = (s+e)//2
        if a[mid]==key:
            return f"value found in the index of {mid}"
        if a[mid]>key:
            e = mid-1
        else:
            s = mid+1
    return "not found"

a = [10,4,7,9,16,6]
print(Binary_search(7))