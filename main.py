
name: str
description: str
price: float

list_names: list = []
list_description: list = []
list_price: list = []

def menu():
    print("MENU:")
    print('1 - Adicionar novo produto')
    print('2 - Ver produtos cadastrados')
    print('3 - Editar produto')
    print('4 - Deletar produto')
    print('5 - Sair')
    print('')
    option = input('Digite a opção escolhida (use os números): -> ')
    return option

def add():
    name = input("Digite o nome do novo produto: ")

    if name in list_names:
        print('')
        print('O PRODUTO JÁ EXISTE!')
        print('')
        pass
        
    else:
        list_names.append(name)
        description = input("Inclua uma breve descrição: ")
        list_description.append(description)
        price = input("Adicione o preço: ")
        list_price.append(price)
        print('')
        print('PRODUTO ADICIONADO!')
        print('')
        pass


def get_products(): 
    print('LISTA DE PRODUTOS: ', list_names) 
    pass 

def delete():
    print('')
    element = input('Digite o nome do produto que deseja excluir: ')
    if element in list_names:
        index = list_names.index(element)
        list_names.pop(index)
        list_description.pop(index)
        list_price.pop(index)
        print('')
        print('ITEM EXCLUIDO!')
        print('')
        pass
    else:
        print('')
        print('PRODUTO NÃO CADASTRADO!')
        print('')

def edit_products():
    print('')
    element = input('Digite o nome do produto que deseja editar: ')
    if element in list_names:
        index = list_names.index(element)
    
        name = input('Digite o novo nome do produto: ')
        if name == '':
            pass
        else:
            list_names[index] = name
            pass

        description = input('Digite a nova descrição do produto: ')
        if description == '':
            pass
        else:
            list_description[index] = description
            pass

        price = input('Digite o novo preço do produto: ')
        if price == '':
            pass
        else:
            list_price[index] = price
            pass
    else:
        print('')
        print('PRODUTO NÃO CADASTRADO!')
        print('')


opcao = menu()
while opcao != '5':
    if opcao == '1':
        add()
    elif opcao == '2':
        get_products()
    elif opcao == '3':
        edit_products()
    elif opcao == '4':
        delete()
    

    opcao = menu()
    