def selection_sort():

    for phase in range(len(a)-1):
        min = phase
        for i in range(phase+1,len(a)):
            if a[i]<a[min]:
                min = i
        a[phase],a[min] = a[min],a[phase]


a = [33,45,38,2,14,16]
selection_sort()
print(a)