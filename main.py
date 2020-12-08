import os 
from products import Product
from categories import Categories

def menu():
    print('')
    print("MENU:")
    print('')
    print('1 - PRODUTOS')
    print('2 - CATEGORIAS')
    print('0 - Sair')
    print('')
    option = int(input('Digite a opção escolhida (use os números): -> '))
    return option

os.system('clear')
product = Product()
categories = Categories()

opcao = menu()

while opcao != 0:
    if opcao == 1:
        os.system('clear')
        opcao_products = product.product_menu()
        while opcao_products != 0:
            if opcao_products == 1:
                os.system('clear')
                product.add()
            elif opcao_products == 2:
                os.system('clear')
                product.get_products()
            elif opcao_products == 3:
                os.system('clear')
                product.edit_products()
            elif opcao_products == 4:
                os.system('clear')
                product.delete()
    
            opcao_products = product.product_menu()
    elif opcao == 2: 
        os.system('clear')
        opcao_categories = categories.categories_menu()   
        if opcao_categories == '1':
            os.system('clear')
            categories.add()
        elif opcao_categories == '2':
            os.system('clear')
            categories.edit()
        elif opcao_categories == '3':
            os.system('clear')
            categories.delete()

    opcao = menu()
