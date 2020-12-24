l = []
a = input()
while a:
    l.append(int(a))
    a = input()
print(*l)
print(sum(l))
print(max(l))