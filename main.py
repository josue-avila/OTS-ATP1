
class Product:
    name: str
    description: str
    price: float

    list_names: list = []
    list_description: list = []
    list_price: list = []

    def menu(self):
        print("MENU:")
        print('1 - Adicionar novo produto')
        print('2 - Ver produtos cadastrados')
        print('3 - Editar produto')
        print('4 - Deletar produto')
        print('5 - Sair')
        print('')
        self.option = input('Digite a opção escolhida (use os números): -> ')
        return self.option

    def add(self):
        name = input("Digite o nome do novo produto: ")

        if name in self.list_names:
            print('')
            print('O PRODUTO JÁ EXISTE!')
            print('')
            pass
            
        else:
            self.list_names.append(name)
            description = input("Inclua uma breve descrição: ")
            self.list_description.append(description)
            price = input("Adicione o preço: ")
            self.list_price.append(price)
            print('')
            print('PRODUTO ADICIONADO!')
            print('')
            pass


    def get_products(self): 
        print('LISTA DE PRODUTOS: ', self.list_names) 
        pass 

    def delete(self):
        print('')
        element = input('Digite o nome do produto que deseja excluir: ')
        if element in self.list_names:
            index = self.list_names.index(element)
            self.list_names.pop(index)
            self.list_description.pop(index)
            self.list_price.pop(index)
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
        if element in self.list_names:
            index = self.list_names.index(element)
        
            name = input('Digite o novo nome do produto: ')
            if name == '':
                pass
            else:
                self.list_names[index] = name
                pass

            description = input('Digite a nova descrição do produto: ')
            if description == '':
                pass
            else:
                self.list_description[index] = description
                pass

            price = input('Digite o novo preço do produto: ')
            if price == '':
                pass
            else:
                self.list_price[index] = price
                pass
        else:
            print('')
            print('PRODUTO NÃO CADASTRADO!')
            print('')

product = Product()

opcao = product.menu()
while opcao != '5':
    if opcao == '1':
        product.add()
    elif opcao == '2':
        product.get_products()
    elif opcao == '3':
        product.edit_products()
    elif opcao == '4':
        product.delete()
    

    opcao = product.menu()
    