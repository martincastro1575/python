from random import choices

tirar = True
while tirar:
    nums = choices([1, 2, 3, 4, 5, 6], k=2)
    print(f'\nDado 1: {nums[0]}\n'
          f'Dado 2: {nums[1]}\n'
          f'Suma: {sum(nums)}\n')

    de_nuevo = 'x'
    while de_nuevo not in 'sSnN':
        de_nuevo = input('Tirar de nuevo? (S/N) ')
        if de_nuevo.upper() == 'N':
            tirar = False