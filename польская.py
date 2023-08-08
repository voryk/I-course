def pol():
    polzap = list(map(str, input('Введите польскую запись через пробел: ').split()))
    mat = ["+", "-", "*", "/"]
    s = []
    if len(polzap) == 0:
        return print('0')
    else:
        for a in polzap:
            if a not in mat:
                s.append(a)
            else:
                b = int(s.pop())
                c = int(s.pop())
                if a == "+":
                    s.append(str(c + b))
                elif a == "-":
                    s.append(str(c - b))
                elif a == "*":
                    s.append(str(c * b))
                elif a == "/":
                    s.append(str(int(c / b)))
    return print(*s)
pol()
