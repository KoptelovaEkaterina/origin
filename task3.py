a = input()
vowel = 'aeiou'
d = {} 
for letter in a:
    if letter in vowel:
        d[letter] = d.get(letter,0) + 1
    else:
        print(letter,end = "")

print()
print(*list(d.keys()))
print(len(d.keys()))
print(d)