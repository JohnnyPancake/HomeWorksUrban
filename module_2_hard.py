def generate_pass(n):
    password = ''
    for i in range(1, n):
        for j in range(i + 1, n):
            if n % (i + j) == 0:
                password += str(i) + str(j)
    return password

print("Введите число от 3 до 20: ")
print(generate_pass(int(input())))
