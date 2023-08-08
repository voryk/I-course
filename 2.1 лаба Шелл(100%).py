from random import randint

strok=int(input('столбов в массиве: '))
stolb=int(input('строк в массиве: '))

arr=[]
for i in range (stolb):
        a=[randint(0,100) for i in range (strok)]
        arr.append(a)

print('Массив до стортировки' )
print(arr)
sortir=[]
sh=0
otv=0

def qwe(a):
    xs=stolb//2 
    while xs>0:
        for i in range (xs,len(a)):#наше число в диапозоне шага
            j=i
            while j>=xs and a[j]<a[j-xs]:# пока номер шанего чилса больше чем наш шаг и есть эелементы, которые меньше нашего
                a[j],a[j-xs] = a[j-xs],a[j]
                j-=xs #делаем ещё один шаг назад
        xs//=2
    return a


for m in range(strok):
        for n in range(stolb):
            sortir.append(arr[n][m])
            sh+=1
            if stolb==sh:
                qwe(sortir)
                for i in range(len(sortir)):
                    arr[i][otv]=sortir[i]
                otv+=1
                sh=0
                sortir=[]

print('Массив после стортировки')
print(arr)
