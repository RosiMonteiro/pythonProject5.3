print('Bem vindo a caça ao tesouro na ilha misteriosa! E Boa sorte!!! ' '\n')

encontrarTesouro = True

while encontrarTesouro:

    escolha = input('Faça a sua escolha: (Selva, Ponte ou Caverna)?' '\n')

    if escolha == 'caverna':
        print('Você, encontrou com o Urso, tente novamente!''\n')

    elif escolha == 'ponte':
        print('Caminho de Risco, tente outro caminho!''\n')

    elif escolha == 'selva':
          encontrarTesouro = False
else:
    print('Você está preste a encotra o Tesouro... Parabénsssssssssss!')















