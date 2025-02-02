import random

letras_maiusculas = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
letras_minusculas = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numeros = ['1','2','3','4','5','6','7','8','9','0']
caracteres_especiais = ['@','#','%','&'] 
todos_caracteres = letras_maiusculas + letras_minusculas + numeros + caracteres_especiais

def gerador_senhas(tamanho_senha):
    senha = ''.join(random.choice(todos_caracteres) for i in range(tamanho_senha))
    return senha

while True:
    tamanho_senha = int(input("Qual o tamanho da senha desejada? (mínimo 12 caracteres) "))
    quantidade_senha = int(input("Quantas senhas deseja gerar? (máximo 10 senhas) "))

    if quantidade_senha > 10:
        print("Digite uma quantidade igual ou menor que 10.")
    elif tamanho_senha < 12 or tamanho_senha > 16:
        print("Peça uma senha entre 12 a 16 caracteres.")
    else:
        for q in range(quantidade_senha):
            senha = gerador_senhas(tamanho_senha) 
            print(f"Sua senha gerada é: {senha}")
        break

