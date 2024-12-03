# Solicite o usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.
def even_odd_calculator1():
    your_number1 = int(input('Insira um número para identificar se é par ou ímpar: \n'))

    if your_number1 % 2 == 0:
        print('Seu número é PAR.\n')
    else:
        print('Seu número é ÍMPAR. \n')

def even_odd_calculator2():
    your_number = int(input('Insira um número para identificar se é par ou ímpar: \n'))
    print (f"O número {your_number} é {'par' if your_number % 2 == 0 else 'ímpar'}.")

def even_odd_calculator3():
    while True:
        try:
            your_number = int(input("Insira um número para identificar se é par ou ímpar: \n"))
            print(f"O número {your_number} é {'par' if your_number % 2 == 0 else 'ímpar'}.")
            break
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro.\n")

def even_odd_calculator4():
        try:
            your_number = list(map(int, input("Digite números separados por espaço: \n").split()))
            for num in your_number:
                print(f"O número {num} é {'par' if num % 2 == 0 else 'ímpar'}.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro.\n")
# Pergunta ao usuário sua idade e, com base nisso, use uma estrutura if elif else pra classificar a idade em categorias de acordo com as seguintes condições:
def user_age_function():
    user_age = int(input('Qual é sua idade?\n'))

    # Criança: 0 a 12 anos.
    if user_age <= 12:
        print('O usuário é criança.')
    # Adolescente: 13 a 18 anos.
    elif 13 <= user_age < 18:
        print('O usuário é adolescente.')
    # Adulto: acima de 18 anos.
    elif user_age >= 18:
        print('O usuário é adulto.')
    else:
        print('Valor inválido.')

#Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.
def user_pass_check():
    username = 'tstorqueto'
    password = 'gato123'
    
    username_input = input('Insira seu nome de usuário.\n')
    password_input = input('Insira sua senha.\n')

    if username_input == username and password_input == password:
        print('Acesso Permitido!')
    else:
        print('Acesso Negado!')

# Scolicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma estrutura if elif else para determinar em qual quadrante do plano cartesiano o ponto se encontra de acordo com as seguintes condições
def coordinates():
    coordinate_x = int(input("Insira o valor x da coordenada:\n"))
    coordinate_y = int(input("Insira o valor y da coordenada:\n"))
    
    if x > 0 and y > 0:
        print("O ponto está no primeiro quadrante.")
    elif x < 0 and y > 0:
        print("O ponto está no segundo quadrante.")
    elif x < 0 and y < 0:
        print("O ponto está no terceiro quadrante.")
    elif x > 0 and y < 0:
        print("O ponto está no quarto quadrante.")
    else:
        print("O ponto está sobre um eixo ou na origem.")


def main():
    user_pass_check()

if __name__ == '__main__':
    main()