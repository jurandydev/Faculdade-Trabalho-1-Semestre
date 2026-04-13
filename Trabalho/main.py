#Integrantes do grupo:

#Jurandy dos Santos Neto  RGM:47042575
#Lucas Yudi Ikiura        RGM:47609893
#Heloysa Lombardi Leme    RGM:46989412
#Felipe Moura Cardoso     RGM:47441089
#Gabriel Gabrigna Queiroz RGM:46903992

#Primeiramente solicitarei o nome do gestor e logo após solicitare o mês de referência.

nome_gestor = input('Digite o seu nome: ')
mes_referencia = input('Digite o mês de referência: ')

#Em seguida, solicitarei quantos dias de venda serão registrados deste mês usando o while pois se caso o usuário digitar um valor igual 0 ou negativo, o programa irá solicitar novamente um valor.
dias_venda = int(input(f'Digite quantos dias de venda serão registrados no mês {mes_referencia}: '))
while dias_venda <= 0:
    print("Dia inválido! Digite um valor maior que 0.")
    dias_venda = int(input(f'Digite quantos dias de venda serão registrados no mês {mes_referencia}: '))

print("\n")

#Agora solicitarei o valor de vendas em cada dia desse mês.
total_vendas = 0
maior_venda = 0
menor_venda = 0
dia_maior = 0
dia_menor = 0
dia_sem_venda = 0

#Agora calcularemos o total de vendas usando o while para não permitir que o usuário coloque um valor negativo.

for i in range(1, dias_venda + 1):
    valor = float(input(f'Digite o valor de venda do {i}º dia: '))
    while valor < 0:
        print("Número inválido! O valor da venda não pode ser negativo. Digite novamente.")
        valor = float(input(f'Digite o valor de venda do {i}º dia: '))
    
    total_vendas = total_vendas + valor
    
#Calculremos o dia com maior venda.
    if valor > maior_venda:
        maior_venda = valor
        dia_maior = i

#Para calcular o dia com menor venda, precisamos considerar o primeiro dia como referência, usando IF e ELIF para comparar os valores.
    if i == 1: 
        menor_venda = valor
        dia_menor = i
    elif valor < menor_venda:    
        menor_venda = valor
        dia_menor = i

#Agora calcularemos os dias que não houveram vendas ou seja o valo foi igual a 0.
    if valor == 0:
        dia_sem_venda = dia_sem_venda + 1  

# Agora a média de vendas diárias.
media_vendas = total_vendas / dias_venda

#Relatóriio Final

print("\n----------Relatório Final----------\n")
print(f' Nome do gestor: {nome_gestor}')
print(f' Mês de referência: {mes_referencia}')
print(f' Total vendido: R$ {total_vendas:.2f}')
print(f' Média de vendas: R$ {media_vendas:.2f}')
print(f' Maior venda: R$ {maior_venda:.2f} (Dia {dia_maior})')
print(f' Menor venda: R$ {menor_venda:.2f} (Dia {dia_menor})')

if dia_sem_venda > 0:
    print(f' Quantidade de dias sem vendas: {dia_sem_venda}')
else:
    print(" Não houve dia sem venda.")

#Agora calcularemos o desempenho do mês em relação a meta.
meta = 10000
desempenho = total_vendas / meta

if total_vendas >= meta: 
    print(' Parabéns! A meta foi atingida!')
    
if desempenho < 0.85:
    print(' O Aproveitamento foi Regular.')
elif desempenho <= 1.0:
    print(' O Aproveitamento foi Bom.')
elif desempenho < 1.25:
    print(' O Aproveitamento foi Ótimo.')
else:
    print(' O Aproveitamento foi Excelente.')