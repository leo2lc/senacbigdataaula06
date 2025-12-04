# Automatizar o cálculo de médias escolares;
# processar notas de 10 estudantes;
# 1 - solicitar as 4 notas, uma a uma
# 2 - Calcular a média
# 3 - Exibir o resultado conforme a regra
#  - Média a partir de 7: "Aprovado"
#  - Média a entre 5 e 7: "Recuperação"
#  - Média abaixo de 5: "Reprovado"

soma = 0
media = 0

for i in range(4):
    nota = float(input('Digite a nota: '))
    soma += nota
    print(f'A nota foi {i + 1}: {nota}')
media = soma / 4
print(f'a média foi: {media}')

match media:
    case m if m >= 7:
        print(f'Aprovado, média: {media}') 
    case m if 5 <= m < 7:
        print(f'Em recuperação, média: {media}')
    case m if m <= 5:
        print(f'Reprovado, média: {media}')