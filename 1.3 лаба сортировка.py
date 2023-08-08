import time
a = []
n = int(input())
for i in range(n):
    e = int(input())
    a.append(e) 
print("Было ", a)

start = time.time()

def sort(a):
    for i in range(1, len(a)):
        m = a[i]
        j = i - 1
        while (j >= 0 and m < a[j]):
            a[j+1] = a[j]
            j = j - 1
        a[j + 1] = m
sort(a)
print("Стало", a)
end=time.time()
print("Время", end-start)
