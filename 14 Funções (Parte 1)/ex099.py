def maior(* num):
    print('-=' * 15)
    print('Analisando os valores passados...' if len(num) == 0 else print(f'Analisando os valores passados {num}...'))
    print(f'Foram informados {len(num)} valores ao todo.')
    print('O maior valor informado foi 0' if len(num) == 0 else print(f'O maior valor informado foi {max(num)}.'))


maior(6, 5, 3, 10, 14, 17)
maior(5, 12, 50, 23, 30)
maior()