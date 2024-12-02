import os

def exibir_nome_do_programa():
    print('𝕾𝖆𝖇𝖔𝖗 𝕰𝖝𝖕𝖗𝖊𝖘𝖘\n')

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair \n')

def finalizar_app():
    os.system('cls')
    print('Finalizando o app.\n')

def escolher_opcao():
    # o input é transformado em inteiro logo após sua inserção.
    opcao_escolhida = int(input('Escolha uma opção: '))
    match opcao_escolhida:
        case 1:
            print('Cadastrar restaurante.')
        case 2:
            print('Listar restaurantes.')
        case 3:
            print('Ativar restaurante.')
        case 4:
            finalizar_app()
        case _:
            print('Opção inválida.')

    # if opcao_escolhida == 1:
    #     print('Cadastrar restaurante')
    # elif opcao_escolhida == 2:
    #     print('Listar restaurantes')
    # elif opcao_escolhida == 3:
    #     print('Ativar restaurante')
    # else:
    #     finalizar_app()

def main():
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()
