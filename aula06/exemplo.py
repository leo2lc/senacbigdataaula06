# Estrutura de repetição "for"

for n in range(5):
    print('Olá mundo!')

# Exemplo de Contagem
    
for num in range(10):
    print(num)

# Exemplo - Contagem de 10 a 20

for i in range(10, 21):
    print(i)

# Exemplo - Contagem de 10 a 100 de dez em dez

for i in range(10, 101, 10):
    print(i)

# Usuário escolhe início e fim

inicio = int(input('informe o início: '))
fim = int(input('Digite o valor final: '))

for n in range(inicio, fim):
    print(n)

# Numerando com a variável do intervalo

for num in range(3):
    print(f'Pessoa {num + 1}: ')
    nome = input('Informe o nome: ')
    print(f'O nome é {nome}')

# Variável acumuladora

total = 0           # uma variável não pode aparecer num calculo sem ser inicializada

for n in range(5):
    numero = float(input('Informe o valor da venda: '))
    total = total + numero

print(f'O total é {total:.2f}') # para formatar casas decimais depois da vírgula
