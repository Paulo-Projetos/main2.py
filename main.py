
def print_hi(name):

    print(f'Hi, {name}')
    print('Oi, ' + name)

def calcular_area_do_retangulo(largura, comprimento):
    return largura * comprimento

def calcular_area_do_quadrado(lado):
    return (lado ** 2)

def calcular_area_do_triangulo(base,altura):
    return ((base * altura)/2)

def contagem_progressiva (fim):
    for numero in range (fim):
        print(numero)

def apoiar_candidato (nome,vezes):
    for numero in range (vezes):
        contador = numero+1
        print(f'{contador} - {nome}')
    # Outra maneira de fazer
    if numero<=9:
        print(f'00{numero+1} - {nome}')
    elif numero<99:
        print(f'0{numero + 1} - {nome}')
    else:
        print(f'{numero+1} - {nome}')

    #Brincadeira do plim
def brincadeira_de_plim(fim):
    for numero in range(fim):
        if numero % 4 == 0:
            print('Plim')
        else:
            print('{:0>3}'.format(numero))


if __name__ == '__main__':
    print_hi('Paulo')

    resultado = calcular_area_do_retangulo(3,4)
    print(f'A área do retangulo é de: {resultado} m²')

    resultado = calcular_area_do_quadrado(5)
    print(f'A área do quadrado é de: {resultado} m²')

    resultado = calcular_area_do_triangulo(6,8)
    print(f'A área do triangulo é de: {resultado} m²')

    #Contagem progressiva de 0 a 10
    contagem_progressiva(10)

    # numero de vezes que do candidato
    apoiar_candidato('Paulo',8)

    #brincar de plim
    brincadeira_de_plim(100)
