def gen_pass(n):
    result = ""
    if n < 3 or n > 20:
        print('Число от 3 до 20! Вас съели!')
    else:
        for i in range(1, n):
            for j in range(i + 1, n):
                if n % (i + j) == 0:
                    result += f"{i}{j}"
        print("Пароль для числа ", n, ": ", result)

gen_pass(int(input("Введите число из первого поля: ")))


