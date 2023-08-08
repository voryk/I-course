from random import randint
mas=int(input('чисел в массиве '))
q=[randint(-100,100) for i in range (mas)]

def slin2(a,b): #Объединяет списки
    c=[]
    i=j=0 #Указатели
    while i<len(a) and j<len(b):
        if a[i]<b[j]:
            c.append(a[i])
            i+=1
        else:
            c.append(b[j])
            j+=1
                  #Какой- либо список может остаться, поэтому вставляем оставшийся в список а
    if i<len(a):
        c+=a[i:]
    if j<len(b):
        c+=b[j:]
    return c
    
def slin(q): #Сортировка
    if len(q)==1: #То список отсортирован
        return q
    mid=len(q)//2
    left=slin(q[:mid])
    right=slin(q[mid:])
    return slin2(left,right) #Объединение

print('Массив до стортировки')
print(q)
print('Массив после сортировки')
print(slin(q))
