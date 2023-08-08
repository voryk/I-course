def scobki():
    a =(input("Введите скобочную последовательность: "))
    s = []
    for i in a:
        if i in ["(", "{", "["]:
            s.append(i)
        else:
            if not s:
                return print(False)
            b = s.pop()
            if b == '(':
                if i != ")":
                    return print(False)
            if b == '{':
                if i != "}":
                    return print(False)
            if b == '[':
                if i != "]":
                    return print(False)
    if s: #Если stack пустой, то выводит ложь
        return print(False)
    return print(True)
scobki()
