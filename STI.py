PORYADOK = ["первое", "второе", "третье", "четвёртое", "пятое", "шестое", "седьмое", "восьмое", "девятое"]
DO = dict()
PRIMER = ''


def making():
    global DO
    global PRIMER
    while '(' in PRIMER or ')' in PRIMER:  # Пример ещё не преобразован
        opening = list()
        closing = list()
        for i in range(len(PRIMER)):  # Индексы начала и конца скобок
            if PRIMER[i] == '(':
                opening.append(i)
            elif PRIMER[i] == ')':
                closing.append(i)
        meen = 100  # Минимальный размер скобок
        final = []
        counted = []
        for op in opening:  # Расстояния от начал скобок до концов
            for cl in closing:
                if cl > op:
                    counted.append(cl - op)
                    if 0 < cl - op < meen:
                        meen = cl - op
            final.append(counted[:])
            counted.clear()
        flag = 0  # Пример изменился
        for op in range(len(final)):
            for long in range(len(final[op])):
                if final[op][long] == meen:
                    start = opening.pop(op)
                    end = closing.pop(closing.index(final[op][long] + start))
                    DO[PORYADOK[len(DO)]] = PRIMER[start + 1:end]
                    PRIMER = PRIMER.replace(PRIMER[start:end + 1], PORYADOK[len(DO) - 1])  # Замена действий
                    flag = 1
                    break
            if flag:
                break


def preps(rest, dct, value):
    new_value = value
    for tri in dct.keys():  # Заменяет предыдущие действия на их результат
        if tri in new_value:
            new_value = str(new_value.replace(tri, str(dct[tri])))
    for letter in rest.keys():  # Заменяет переменные на их значения
        if letter in str(new_value):
            new_value = str(new_value).replace(letter, str(rest[letter]))
    # Кусок кода, который мог облегчить мой прошлый урок (автоматические заменяет импликацию, "или" и "и")
    if 'или' in new_value:
        new_value = str(new_value).replace('или', 'or')
    if 'и' in new_value:
        new_value = str(new_value).replace('и', 'and')
    if '->' in new_value:
        new_value = new_value.split(' -> ')
        new_value = f'not {new_value[0]} or {new_value[1]}'
    return new_value


def count(do, **rest):  # Вычисления
    leest = list()
    dct = do.copy()
    for key in dct.keys():
        value = preps(rest, dct, dct[key])
        dct[key] = str(int(eval(value)))
        leest.append(dct[key])
    return leest


def main():
    global DO
    global PRIMER
    PRIMER = '(' + input('Введите пример:\n') + ')'
    num_of_perem = 0
    if 'x' in PRIMER:
        num_of_perem += 1
        if 'y' in PRIMER:
            num_of_perem += 1
            if 'z' in PRIMER:
                num_of_perem += 1
                if 'w' in PRIMER:
                    num_of_perem += 1
    making()  # Преобразование
    print('Нужен вывод целиком или только с определённым ответом',
          'Введите 0 или 1 если нужен определённый или нажмите "enter" чтобы вывести целиком', sep='\n')
    inpt = input()
    if inpt != '' and inpt in '01':
        need_smth = True
        need = int(inpt)
    else:
        need_smth = False
        need = None
    print('x y z w'[:num_of_perem * 2], '1 2 3 4 5 6 7 8 9'[:len(DO.keys()) * 2 - 1], '\n', sep='  ')
    for x in range(2):
        for y in range(2):
            if num_of_perem > 2:
                for z in range(2):
                    if num_of_perem > 3:
                        for w in range(2):
                            sleest = count(DO, x=x, y=y, z=z, w=w)
                            if not need_smth or (need_smth and int(sleest[-1]) == need):
                                print(f'{x} {y} {z} {w} ', *sleest)
                    else:
                        sleest = count(DO, x=x, y=y, z=z)
                        if not need_smth or (need_smth and int(sleest[-1]) == need):
                            print(f'{x} {y} {z} ', *sleest)
            else:
                sleest = count(DO, x=x, y=y)
                if not need_smth or (need_smth and int(sleest[-1]) == need):
                    print(f'{x} {y} ', *sleest)


main()
