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
    '''Está função exibe as opções interátivas com o usuário.
    
    Inputs:
    - 1
    - 2
    - 3
    - 4    
    '''
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Alternar estado do Restaurante')
    print('4. Sair\n')
def finalizar_app():
    subtitulo_menu_opcao('Finalizando app!')
def opcao_invalida():
   print('opcâo inválida!!!')
   voltar_menu_principal()
def avaliar_opcao_escolhida():
    '''
    Está funções identifica a opcao escolhida pelo usuário e retorna uma função específica.

    Inputs:
    - 1
    - 2
    - 3
    - 4 

    Outputs:
    - cadastrar_restaurantes()
    - listar_restaurantes()
    - opcao_ativar_restaurante()
    - finalizar_app()
    - opcao_invalida()
    '''
    try:
        opcao_escolhida = int(input('Escolha uma Opção: '))
        if opcao_escolhida == 1:
            cadastrar_restaurantes()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            opcao_ativar_restaurante()
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
    linha = '*' * len(texto)
    print(linha)
    print(f"{texto}")
    print(f'{linha}\n')
# funcões de avaliação das opções escolhidas
def cadastrar_restaurantes():
    '''
    Está função cadastra novo restaurantes e retorna uma nova lista.

    Inputs:
    - nome
    - categoria
    - estado

    Outputs:
    - lista com novo restaurante
    '''
    subtitulo_menu_opcao('Cadastro oficial de novos retaurantes:')
    nome_restaurante_da_vez = str(input('Qual o nome do resturante que desejas cadastrar? '))
    categoria_do_restaurante = str(input(f'Qual a categoria do restaurante {nome_restaurante_da_vez}? '))
    dados_do_restaurante = {'nome': nome_restaurante_da_vez, 'categoria': categoria_do_restaurante, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f'| O restaurante: {nome_restaurante_da_vez} | categoria: {categoria_do_restaurante} | foi cadastrado com sucesso!')
    voltar_menu_principal()
def listar_restaurantes():
    '''
    Está função irá listar todos os restaurantes e retornar em uma lista organizada

    Inputs:
    - nome
    - categoria
    - estado

    Outputs:
    - lista organizada
    
    '''
    subtitulo_menu_opcao('Listagem oficial de retaurantes:')
    print(f'{'Nome dos restaurantes:'.ljust(20)} | {'Categoria:'.ljust(20)} | {'Estado:'}\n')
    for restaurante in restaurantes:
        nome = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'Desativado'
        print(f'- {nome.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    voltar_menu_principal()
def opcao_ativar_restaurante():
    '''
    Está função irá mudar o estado no qual o restaurante se encontra.

    Inputs:
    - nome do restaurante
    - estado

    Outputs:
    - mudança de estado

    '''
    subtitulo_menu_opcao("Cadastro de ativação de restaurantes oficial!")
    nome_do_restaurante = input('Qual o nome do restaurante que deseja ativar? ')
    restaurante_ativo = False
    for restaurante in restaurantes:
        if nome_do_restaurante == restaurante['nome']:
            restaurante_ativo = True
            restaurante['ativo'] = not restaurante['ativo']
            if( restaurante['ativo'] == True):
                print(f"O restaurante {nome_do_restaurante} foi Ativado com sucesso!")
            else:
                print(f"O restaurante {nome_do_restaurante} foi Desativado com sucesso!")
    if not restaurante_ativo:
        print("Restaurante não encontrado")
            


    voltar_menu_principal()
def main():
    os.system('cls')
    exibir_nome_app()
    exibir_opcoes()  
    avaliar_opcao_escolhida()
if __name__ == '__main__':
    main()