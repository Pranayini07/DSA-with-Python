def bubble_sort():
    for phase in range(1,len(a)):
        flag = 0
        for i in range(len(a)-phase):
            if a[i]>a[i+1]:
                flag=1
                a[i],a[i+1]=a[i+1],a[i]
        if flag==0: return

a = [33,45,38,2,14,16]
bubble_sort()
print(a)