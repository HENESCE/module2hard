def keys(n):
    password = ''
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            if n % (i + j) == 0:
                password += str(i) + str(j)
    return password

for n in range(3, 21):
    password = keys(n)
    print(f"{n} - {password}")