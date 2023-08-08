from random import randint
a=[]
print('Введите кол-во чисел:')
gg=int(input())
for i in range(gg):
    a.append(randint(-100,100))
a.sort()
print('Сам массив')
print(a)
print('Что будем искать?')
ind=int(input())
mid=len(a)//2
n=0
v=len(a)-1
while a[mid]!=ind and n<=v:
    if ind>a[mid]:
        n=mid+1
    else:
        v=mid-1
    mid=(v+n)//2
if ind==a[mid]:
    print('index:', mid)
else:
    print('Элемент в массиве не найден')
