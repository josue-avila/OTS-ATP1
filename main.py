import os 

class Product:
    name: str
    description: str
    price: float

    list_products: list = []
    list_product: list = ['','','']

    def menu(self):
        print("MENU:")
        print('')
        print('1 - Adicionar novo produto')
        print('2 - Ver produtos cadastrados')
        print('3 - Editar produto')
        print('4 - Deletar produto')
        print('5 - Sair')
        print('')
        self.option = input('Digite a opção escolhida (use os números): -> ')
        return self.option

    def add(self):
        name= input("Digite o nome do novo produto: ")

        if any(name in self.list_product for self.list_product in self.list_products):
            print('')
            print('O PRODUTO JÁ EXISTE!')
            print('')
            pass
            
        else:
            description = input("Inclua uma breve descrição: ")
            price = input("Adicione o preço: ")
       
            self.list_product = [name,description,price]
            self.list_products.append(self.list_product)

            print('')
            print('PRODUTO ADICIONADO!')
            print('')
            pass


    def get_products(self):
        print('')
        print('LISTA DE PRODUTOS: ', self.list_products) 
        print('')
        pass 

    def delete(self):
        print('')
        element = input('Digite o nome do produto que deseja excluir: ')
        if any(element in self.list_product for self.list_product in self.list_products):
            index = [i for i, j in enumerate(self.list_products) if element in j][0] 
            self.list_products.pop(index)

            print('')
            print('ITEM EXCLUIDO!')
            print('')
            pass
        else:
            print('')
            print('PRODUTO NÃO CADASTRADO!')
            print('')

    def edit_products(self):
        print('')
        element = input('Digite o nome do produto que deseja editar: ')
        if any(element in self.list_product for self.list_product in self.list_products):
            index = [i for i, j in enumerate(self.list_products) if element in j][0]
            index1 = self.list_products[index].index(element)
            print(index)
            name = input('Digite o novo nome do produto: ')
            if name == '':
                pass
            else:
                self.list_products[index][index1] = name
                pass

            description = input('Digite a nova descrição do produto: ')
            if description == '':
                pass
            else:
                self.list_products[index][index1+1] = description
                pass

            price = input('Digite o novo preço do produto: ')
            if price == '':
                pass
            else:
                self.list_products[index][index1+2] = price
                pass
        else:
            print('')
            print('PRODUTO NÃO CADASTRADO!')
            print('')

os.system('clear')
product = Product()

opcao = product.menu()

while opcao != '5':
    if opcao == '1':
        os.system('clear')
        product.add()
    elif opcao == '2':
        os.system('clear')
        product.get_products()
    elif opcao == '3':
        os.system('clear')
        product.edit_products()
    elif opcao == '4':
        os.system('clear')
        product.delete()
    

    opcao = product.menu()
    