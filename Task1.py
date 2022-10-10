# вход - строка. вычислить арифметическое выражение, заданое строкой (+, -, /, *)
# Добавить скобки.
actions = {
    "^": lambda x, y: str(float(x) ** float(y)),
    "*": lambda x, y: str(float(x) * float(y)),
    "/": lambda x, y: str(float(x) / float(y)),
    "+": lambda x, y: str(float(x) + float(y)),
    "-": lambda x, y: str(float(x) - float(y))
}


res = "( 10 + 5 ) * 3 - 8 / 2"
def borders(line):
    lst = []
    i = 0
    while i < len(line):
        if line[i] =='(':
            m = line.index(")", i)
            lst.append(line[i+1:m])
            i = m
        else:
            lst.append(line[i])
        i += 1
    return lst


# print(borders(res.split()))

def in_borders(lst):
    for i in range(len(lst)):
        if isinstance(lst[i], list):
            a, b, c = borders(lst[i])
            lst[i] = actions[b](a, c)
    return lst

print(in_borders(borders(res.split())))

def final(lst):
    priority = [i for i, j in enumerate(lst) if j in "*/"]
    while priority:
        t = priority[0]
        a, b, c = lst[t - 1 : t + 2]
        lst.insert(t-1, actions[b](a, c))
        del lst[t : t + 3]
        priority = [i for i, j in enumerate(lst) if j in "*/"]
    
    while len(lst) > 1:
        a, b, c = lst[: 3]
        del lst[: 3]
        lst.insert(0, actions[b](a, c))
        

    return lst

print(final(in_borders(borders(res.split()))))


