i = 0
j = 1

print(i)
print(j)

for x in range(3,51):
    Fn = i + j
    print(Fn)

    i = j
    j = Fn
