l = [2, 3, 5, 7, 11]
a = input() 
while a:
    a = int(a)
    for i in l:
        if a % i == 0:
            print(f"{a} делится на {i}")
    a = input()