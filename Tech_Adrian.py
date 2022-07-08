def linha(cor):
    print(f'{cor}{"___" * 22}\033[m')


produtos = []
valortotal = contagem = 0


# introdução
print(f'\033[1;31;40m{"---"*22}\033[m')
print(f"\033[1;34;40m{'Adrians & Adrians tech store CORP LTDA'.center(66,' ')}\033[m")
print(f'\033[1;31;40m{"---"*22}\033[m')
listadeprodutos = [['Teclado Mecânico Redragon Kumara Switch ABNT2', 262.00],
                   ['Mouse Gamer Razer Deathadder Essential 6400 DP', 100.00],
                   ['Memória Ram HyperX Fury de 8GB DIMM DDR4', 302.90],
                   ['Processador CORE I5-10400F 10ª Geração LGA', 845.00],
                   ['RTX 3060, 12GB GDDR6, GHOST Series', 3412.98],
                   ['SSD Kingston SNVS 500GB padrão NV1', 349.98],
                   ['Cooler Amd/Intel Ice Edge Mini Fs V2.', 69.00],
                   ['Pc Gamer Completo Intel Core i5 10400F', 2939.00]]

# Mostragem dos produtos
print(f'\n\033[1;34;40m Lista de produtos: \033[m')
linha("\033[4;31;40m")
for i, v in enumerate(listadeprodutos):
    print(f'\033[1;34;40m {listadeprodutos[i][0]:.<54}R$', end='')
    print(f'{listadeprodutos[i][1]:>8.2f} \033[m')
linha("\033[9;31;40m")
print()

# Compras
while True:
    compra = input('Que produto você quer comprar? ').strip()
    while compra.strip() == '':
        print('\t\033[1;31mNada foi escrito\033[m')
        compra = input('Que produto você quer comprar? ').strip()
    while compra.isnumeric():
        compra = input('Que produto você quer comprar? (Apenas produtos da lista) ').strip()
    for i, v in enumerate(listadeprodutos):
        if compra.upper() in listadeprodutos[i][0].upper():
            produtos.append([listadeprodutos[i][0], listadeprodutos[i][1]])
            valortotal += listadeprodutos[i][1]
        else:
            contagem += 1
            if contagem == len(listadeprodutos):
                print('\t\033[1;31mproduto não encontrado\033[m')
    contagem = 0
    while True:
        try:
            resposta = input('\tDeseja continuar? ').strip().upper()[0]
        except:
            print('\t\033[1;31mNada foi escrito\033[m')
        else:
            break
    while resposta not in 'SN':
        try:
            resposta = input('\tResposta inválida, deseja continuar? [S/N]').strip().upper()[0]
        except:
            print('\t\033[1;31mNada foi escrito\033[m')
    if resposta == "N":
        break

# Mostragem da compra
if len(produtos) == 0:
    linha("\033[4;31;40m")
    print(f'\033[1;34;40m{"você não comprou nehum produto".center(66)}\033[m')
    linha("\033[9;31;40m")
else:
    print(f'\033[1;34;40m Você comprou os produtos: \033[m')
    linha("\033[4;31;40m")
    for i, v in enumerate(produtos):
        print(f'\033[1;34;40m {produtos[i][0]:.<49}.por R$', end='')
        print(f'{produtos[i][1]:>8.2f} \033[m')
    print(f'\033[1;32;40m{"  ":<18}O valor total é de R$ {valortotal:.2f}{"  ":>19}\033[m')
    linha("\033[9;31;40m")

# Pagamento
while True:
    try:
        if len(produtos) > 0:
            formadepagamento = int(input('''Qual a forma de pagamento?
[1] A vista no dinheiro (10% de desconto)
[2] A vista no débito
[3] Parcelado em até 6x sem juros
[4] Parcelado em 7x ou mais (2% de juros)
Responda aqui: '''))
    except:
        print()
        print(f'\033[1;31m\tApenas numeros, tente novamente.\033[m')
    else:
        if formadepagamento > 4 or formadepagamento < 1:
            print()
            print(f'\033[1;31m\tApenas numeros de 1 à 4\033[m')
        else:
            break
if len(produtos) == 0:
    formadepagamento = 2

# Pagamento 1
if formadepagamento == 1:
    desconto = valortotal*10/100
    valor = valortotal-desconto
    print(f'\n\033[1;32m\tO valor a pagar agora é de R$ {valor:.2f} \033[m')

# Pagamento 2
if formadepagamento == 2:
    print(f'\n\033[1;32m\tO valor a pagar é de R$ {valortotal:.2f} \033[m')

# Pagamento 3
if formadepagamento == 3:
    parcelas = int(input('\n\033[1;32m\tQuantas parcelas? \033[m'))
    if parcelas <= 6:
        valor = valortotal / parcelas
        print(f'\n\033[1;32m\tO valor de cada parcela é de R$ {valor:.2f} \033[m')
    while parcelas > 6:
        troca = input('\n\033[1;32m\tparcelas maiores que 6 recebem juros, '
                      'deseja continuar com esse número de parcelas? \033[m').upper().strip()[0]
        while troca not in 'SN':
            troca = input('\n\033[1;32m\tResposta inválida, '
                          'deseja continuar com esse número de parcelas? [S/N]\033[m').upper().strip()[0]
        if troca in "N":
            parcelas = int(input('\n\033[1;32m\tQuantas parcelas? [menor ou igual a 6] \033[m'))
            if parcelas <= 6:
                valor = valortotal / parcelas
                print(f'\n\033[1;32m\tO valor de cada parcela é de R$ {valor:.2f} \033[m')
                break
        else:
            formadepagamento = 4
            break

# Pagamento 4
if formadepagamento == 4:
    parcelas = int(input('\n\033[1;32m\tQuantas parcelas? \033[m'))
    if parcelas >= 7:
        juros = valortotal * 2 / 100
        valortotal = valortotal + juros
        valor = valortotal / parcelas
        print(f'\n\033[1;32m\tO valor agora é R$ {valortotal:.2f}, '
              f'cada parcela fica por R${valor:.2f} \033[m')
    while parcelas <= 6:
        troca = input('\n\033[1;32m\tparcelas menores que 6 não recebem juros, '
                      'deseja continuar com esse número de parcelas? \033[m').upper().strip()[0]
        while troca not in 'SN':
            troca = input('\n\033[1;32m\tResposta inválida, '
                          'deseja continuar com esse número de parcelas? [S/N]\033[m').upper().strip()[0]
        if troca in "N":
            parcelas = int(input('\n\033[1;32m\tQuantas parcelas? [maior ou igual a 7] \033[m'))
            if parcelas >= 7:
                juros = valortotal * 2 / 100
                valortotal = valortotal + juros
                valor = valortotal / parcelas
                print(f'\n\033[1;32m\tO valor agora é R$ {valortotal:.2f}, '
                      f'cada parcela fica por R${valor:.2f} \033[m')
                break
        else:
            linha("\033[31;40m")
            print(f"\033[1;34;40m{'<<<<< TENTE NOVAMENTE >>>>>'.center(66, ' ')}\033[m")
            linha("\033[31;40m")
            break

# Encerramento
print()
linha("\033[4;31;40m")
print(f"\033[1;34;40m{'<<<<< PROGRAMA ENCERRADO >>>>>'.center(66,' ')}\033[m")
linha("\033[9;31;40m")
