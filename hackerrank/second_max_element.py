#sort the array and print second largest element

a = [2 ,3 ,6 ,6 ,5]

n=len(a)
for i in range(n):
    for j in range(0, n-i-1):
        if a[j]>a[j+1]:
            a[j],a[j+1] = a[j+1], a[j]

a = list(set(a))
print("the second largest element in the list is=",a[-2])