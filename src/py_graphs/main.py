from random import randint

def perebor():
    global mas

    answer = []
    for a in range(1, 10):
        for b in range(a + 1, 10):
            flag = True
            for u in range(len(mas)):
                if mas[u][2] == '>':
                    if not(mas[u][0] * a > mas[u][1] * b):
                        flag = False
                        break
                elif mas[u][2] == '<':
                    if not (mas[u][0] * a < mas[u][1] * b):
                        flag = False
                        break
            if flag: answer.append((a,b))
            # if len(answer) > 1: return False
    print(answer)
    return answer[0] if len(answer) == 1 else False

mas = []
vvod = ''
print('a 2')
koof_a, koof_b = 2, 1
while vvod != '=':
    vvod = input()
    if vvod == '>':
        mas.append([koof_a, koof_b, '>'])
        result = perebor()
        if result == False:
            koof = randint(2, 5)
            koof_b *= koof
            print(f'b {koof}')
        else:
            product = koof_a * result[0] * koof_b * result[1]
            print(f'a {product // (koof_b * result[1])}')
            input()
            print(f'b {product // (koof_a * result[0])}')
    elif vvod == '<':
        mas.append([koof_a, koof_b, '<'])
        result = perebor()
        if result == False:
            koof = randint(2, 5)
            koof_a *= koof
            print(f'a {koof}')
        else:
            product = koof_a * result[0] * koof_b * result[1]
            print(f'a {product // (koof_b * result[1])}')
            input()
            print(f'b {product // (koof_a * result[0])}')