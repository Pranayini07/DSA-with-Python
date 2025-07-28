def insertion_sort():

    for i in range(1,len(a)):
        j = i-1
        temp =a[i]
        while j>=0 and a[j]>temp:
            a[j+1]=a[j]
            j-=1
        a[j+1]=temp

a = [33,45,38,2,14,16]
insertion_sort()
print(a)