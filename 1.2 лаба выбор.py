import time
a=[]
z=int(input())
for t in range(z):
    a.append(int(input()))
print("До -", a)

start=time.time()

i=0
m=0
while i < z-1:
    m=i
    j=i+1
    while j<z:
        if a[j]<a[m]:
            m=j
        j+=1
    a[i], a[m]=a[m], a[i]
    i+=1
print("После - ", a)
end=time.time()
print("Время", end-start)
    
