# Função para cálculo de média onde o usuário informa os valores das notas.

def calcular_media():
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    media = (nota1 + nota2) / 2
    return media

minha_media = calcular_media()
print('Minha média é: ', minha_media)