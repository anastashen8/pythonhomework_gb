# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму
# этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

S = int(input("Сумма чисел: "))
P = int(input("Произведение чисел: "))

for x in range(1, S):
    y = S-x
    if x == P / y:
        print(f'Петя загадал {x} и {y}')
        break
    x += 1
else:
    print('Условия не верны')



