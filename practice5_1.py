a = [int(i) for i in input("Введи список ").split()]
b = int(input("Введи число "))
def large (a = []):
    a.sort(reverse=True)
    s = []
    for i in range(len(a)):
        if a[i] > b:
            s.append(a[i])
    return s
print(large(a))

