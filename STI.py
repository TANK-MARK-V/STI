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
                    DO['|' + str(len(DO)) + '|'] = PRIMER[start + 1:end]
                    PRIMER = PRIMER.replace(PRIMER[start:end + 1], '|' + str(len(DO) - 1) + '|')  # Замена действий
                    flag = 1
                    break
            if flag:
                break


def changing(value):  # Автоматически заменяет знаки
    new_value = value
    dct = {
        ' and ': (' и ', ' ∧ '),  # Конъюнкция
        ' or ': (' или ', ' ∨ '),  # Дизъюнкция
        ' == ': (' = ', ' ≡ '),  # Эквивалентность
        ' <= ': (' -> ', ' → ')  # Имликация
    }
    for put, take in dct.items():
        for get in take:
            new_value = new_value.replace(get, put) if get in new_value else new_value
    if ' <= ' in new_value and 'not' in new_value:
        new_value = new_value.split(' <= ')
        new_value = f'not {new_value[0]} or {new_value[1]}'
    if ' == ' in new_value and 'not' in new_value:
        new_value = new_value.split(' == ')
        new_value = f'({new_value[0]}) == ({new_value[1]})'
    return new_value


def preps(rest, dct, value):
    new_value = value
    for tri in dct.keys():  # Заменяет предыдущие действия на их результат
        if tri in new_value:
            new_value = new_value.replace(tri, str(dct[tri]))
    for letter in rest.keys():  # Заменяет переменные на их значения
        if letter in str(new_value):
            new_value = new_value.replace(letter, str(rest[letter]))
    return changing(new_value)


def make_count(do, **rest):  # Вычисления
    leest = list()
    dct = do.copy()
    for key in dct.keys():
        value = preps(rest, dct, dct[key])
        dct[key] = str(int(eval(value)))
        leest.append(dct[key])
    return leest


def sti(primer, only=''):
    global DO
    global PRIMER
    DO = dict()
    PRIMER = '(' + primer.lower() + ')'
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
    if only != '' and only in '01':
        need_smth = True
        need = int(only)
    else:
        need_smth = False
        need = None
    first_space = "   "
    second_space = " "
    out = 'x y z w'[:num_of_perem * 2] + "  "
    if len(DO.keys()) == 1:
        out += 'F'
    else:
        out += first_space.join([str(i) for i in range(1, len(DO.keys())) if i < 10])
        if len(DO.keys()) >= 10:
            out += second_space + second_space.join([str(i) for i in range(len(DO.keys())) if i >= 10])
        out += first_space + 'F'
    out += '\n'
    for x in range(2):
        if num_of_perem > 1:
            for y in range(2):
                if num_of_perem > 2:
                    for z in range(2):
                        if num_of_perem > 3:
                            for w in range(2):
                                sleest = make_count(DO, x=x, y=y, z=z, w=w)
                                if not need_smth or (need_smth and int(sleest[-1]) == need):
                                    out += f"{x} {y} {z} {w}  " + first_space.join(sleest) + "\n"
                        else:
                            sleest = make_count(DO, x=x, y=y, z=z)
                            if not need_smth or (need_smth and int(sleest[-1]) == need):
                                out += f"{x} {y} {z}  " + first_space.join(sleest) + "\n"
                else:
                    sleest = make_count(DO, x=x, y=y)
                    if not need_smth or (need_smth and int(sleest[-1]) == need):
                        out += f"{x} {y}  " + first_space.join(sleest) + "\n"
        else:
            sleest = make_count(DO, x=x)
            if not need_smth or (need_smth and int(sleest[-1]) == need):
                out += f"{x}  " + first_space.join(sleest) + "\n"
    return out
