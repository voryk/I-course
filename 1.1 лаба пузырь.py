import time
a=[]
z=int(input())
for t in range(z):
    a.append(int(input()))
print("До -", a)

start=time.time()

for i in range(z-1):
    for r in range(z - 1):
        if a[r] > a[r+1]:
            a[r], a[r+1] = a[r+1], a[r]
print("После -", a)
end = time.time()
print("Время", end-start)
