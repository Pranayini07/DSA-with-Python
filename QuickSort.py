def quick(s,e):
    if s<e:
        pi_v = partition(s,e)
        quick(s,pi_v-1)
        quick(pi_v+1,e)

def partition(s , e):
    i = s
    j=e-1
    pivot = arr[e]

    while i<=j:
        while arr[i]<pivot:
            i+=1
        while j>=0 and arr[j]>=pivot:
            j-=1
        if i<j:
            arr[i],arr[j]=arr[j],arr[i]
    arr[e],arr[i]=arr[i],arr[e]
    return i



arr = [4,7,1,8,6,6,5]
quick(0,len(arr)-1)
print(arr)