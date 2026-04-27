import os

restaurantes = [
    { 'nome': 'Hugo', 'categoria': 'pizza', 'ativo': False},
    { 'nome': 'alan', 'categoria': 'hamburguer', 'ativo': True}
]

# funções do menu principal
def exibir_nome_app():
    print('''

    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
    ''')
def exibir_opcoes():
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Ativar Restaurante')
    print('4. Sair\n')
def finalizar_app():
    subtitulo_menu_opcao('Finalizando app!')
def opcao_invalida():
   print('opcâo inválida!!!')
   voltar_menu_principal()
def avaliar_opcao_escolhida():
    try:
        opcao_escolhida = int(input('Escolha uma Opção: '))
        if opcao_escolhida == 1:
            cadastrar_restaurantes()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            print('ativar restaurante')
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida() 
def voltar_menu_principal():
    input('\nDigite alguma tecla para voltar ao menu principal: ')
    main()
def subtitulo_menu_opcao(texto):
    os.system('cls')
    print(f"{texto}\n")
# funcões de avaliação das opções escolhidas
def cadastrar_restaurantes():
    subtitulo_menu_opcao('Cadastro oficial de novos retaurantes:')
    nome_restaurante_da_vez = str(input('Qual o nome do resturante que desejas cadastrar? '))
    categoria_do_restaurante = str(input(f'Qual a categoria do restaurante {nome_restaurante_da_vez}? '))
    dados_do_restaurante = {'nome': nome_restaurante_da_vez, 'categoria': categoria_do_restaurante, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f'| O restaurante: {nome_restaurante_da_vez} | categoria: {categoria_do_restaurante} | foi cadastrado com sucesso!')
    voltar_menu_principal()
def listar_restaurantes():
    subtitulo_menu_opcao('Listagem oficial de retaurantes:')
    for restaurante in restaurantes:
        nome = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = restaurante['ativo']
        print(f'- {nome} | {categoria} | {ativo}')
    voltar_menu_principal()

def main():
    os.system('cls')
    exibir_nome_app()
    exibir_opcoes()  
    avaliar_opcao_escolhida()
if __name__ == '__main__':
    main()