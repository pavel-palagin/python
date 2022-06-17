total = 20
max = 8
gamer = 1
def enter_number():
    err = True
    while err:
        N = int(input('enter number: '))
        if N > max:
            print('>max!!!')
        elif total <= max and N > total:
            print('больше чем конфет на столе')
        else:
            err = False
    return N


end = True
while end:
    if x and gamer ==2:

    print(f'Ход игрока {gamer}')
    take_candy = enter_number()
    total = total - take_candy
    if total <= max:
        max = total
    if total > 1:
        print(f'На столе осталось {total}')
        if gamer == 1:
            gamer = 2
        else:
            gamer = 1
    elif total == 0:
        if gamer == 1:
            gamer = 2
        else:
            gamer = 1
        print(f'победил игрок {gamer}')
        end = False
    else:
        print(f'победил игрок {gamer}')
        end = False





