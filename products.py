import os

from categories import Categories
 

class Product:
    name: str
    description: str
    price: float
    weigth: float
    length: float
    heigth: float
    width: float
    
    list_products: list = []
    list_product: list = ['','','']
    categories: list = []

    
    def product_menu(self) -> int:
        print('')
        print("MENU DE PRODUTOS:")
        print('')
        print('1 - Adicionar novo produto')
        print('2 - Ver produtos cadastrados')
        print('3 - Editar produto')
        print('4 - Deletar produto')
        print('0 - Sair')
        print('')
        self.option = int(input('Digite a opção escolhida (use os números): -> '))
        return self.option

    def add(self):
        name= input("Digite o nome do novo produto: ")
        c = Categories()
        if any(name in list for list in self.list_products):
            print('')
            print('O PRODUTO JÁ EXISTE!')
            print('')
            pass
        else:
            categorie =[]
            while categorie != '0':
                print('')
                print('Selecione as categorias à que o novo produto pertence:')
                print('')
                for j in c.categories:
                    for i in range(len(j)):
                        if i == 0:
                            print('')
                            print(j[i])
                        else:
                            print('     '+str(j[i]))
                categorie = input('Escreva uma de cada vez e quando estiver pronto digite 0 (zero) -> ')
                if any(categorie in list for list in c.categories):
                    self.categories.append(categorie)
                elif categorie == '0':
                    pass
                else:
                    print('')
                    print('CATEGORIA NÃO CADASTRADA')
                    print('')
                    pass
            description = input("Inclua uma breve descrição: ")
            while len(description) < 20:
                print('A decrição deve ter pelo menos 20 caracteres!')
                description = input("Inclua uma breve descrição: ")
            try:
                price = float(input("Adicione o preço (em R$): "))
                while price <=0:
                    price = float(input("O valor precisa ser maior que zero. Digite o valor: "))
                       
            except ValueError as err:
                print("O valor adicionadno é inválido, é preciso usar números")

            else:
                try:
                    weigth = float(input("Adicione o peso do produto (em Kg): "))                
                    print("O valor adicionadno é inválido, é preciso usar números")
                    print('')
                    print("DIMENSÕES - Entre com as medidas do novo produto (em centímetros) ")
                    length = float(input("Comprimento: "))              
                    height = float(input("Altura: "))
                    width = float(input("Largura: "))

                    dimensions = [length, height ,width]
                    self.list_product = [name,description,price, weigth, dimensions, self.categories]
                    self.list_products.append(self.list_product)

                    print('PRODUTO ADICIONADO!')
                    print('')
                    pass
                    
                except ValueError as err:
                    print('')
                    print("O valor adicionadno é inválido.É preciso usar números nos campos: PREÇO, PESEO, E DIMENSÕES")


    def get_products(self):
        print('')
        print('LISTA DE PRODUTOS: ')
        for i in range(len(self.list_products)):
            print('')
            for j in range(6):
                if j == 0:
                    print(str(i + 1) +' - Nome: ', self.list_products[i][j])
                elif j == 1:
                    print('    Descrição: ', self.list_products[i][j])
                elif j == 2: 
                    print('    Preço: R$ ' + str(self.list_products[i][j]))
                elif j == 3: 
                    print('    Peso: ' + str(self.list_products[i][j])+"Kg")
                elif j == 4:
                    print('    Dimensões: ' + str(self.list_products[i][j][0])+'cm x '+str(self.list_products[i][j][1]) +'cm x '+str(self.list_products[i][j][2])+'cm' ) 
                else:
                    print('')
                    print('    Categorias: ')
                    print('    '+str(self.list_products[i][j]))
            print('')
            

    def delete(self):
        print('')
        element = input('Digite o nome do produto que deseja excluir: ')
        if any(element in list for list in self.list_products):
            index = [i for i, j in enumerate(self.list_products) if element in j][0] 
            self.list_products.pop(index)
            self.categories.pop(index)

            print('')
            print('ITEM EXCLUIDO!')
            print('')
            pass
        else:
            print('')
            print('PRODUTO NÃO CADASTRADO!')
            print('')

    def edit_products(self):
        c = Categories()
        print('')
        element = input('Digite o nome do produto que deseja editar: ')
        if any(element in list for list in self.list_products):
            index = [i for i, j in enumerate(self.list_products) if element in j][0]
            index1 = self.list_products[index].index(element)
            name = input('Digite o novo nome do produto: ')
            if name == '':
                pass
            else:
                if any(name in list for list in self.list_products):
                    print('')
                    print('PRODUTO JÁ EXISTE!')
                    print('')
                    pass
                else:
                    self.list_products[index][index1] = name
                    pass
                    
                    categorie = []
                    while categorie != '0':
                        print('')
                        print('Selecione as novas categorias à que esse produto pertence:')
                        print('')
                        for j in c.categories:
                            for i in range(len(j)):
                                if i == 0:
                                    print('')
                                    print(j[i])
                                else:
                                    print('     '+str(j[i]))
                        categorie = input('Escreva uma de cada vez e quando estiver pronto digite 0 (zero) -> ')
                        if any(categorie in list for list in c.categories):
                            self.categories.append(categorie)
                        elif categorie == '0':
                            pass
                        else:
                            print('')
                            print('CATEGORIA NÃO CADASTRADA')
                            print('')
                            pass

                    description = input('Digite a nova descrição do produto: ')
                    if description == '':
                        pass
                    else:
                        while len(description) < 20:
                            print('A decrição deve ter pelo menos 20 caracteres!')
                            description = input("Inclua uma breve descrição: ")
                        self.list_products[index][index1+1] = description
                        pass

                    price = input('Digite o novo preço do produto: ')
                    if price == '':
                        pass
                    else:
                        self.list_products[index][index1+2] = price
                        pass
                    weigth = input('Digite o novo peso do produto: ')
                    if weigth == '':
                        pass
                    else:
                        self.list_products[index][index1+3] = weigth
                        pass
                    length = input('Digite o novo comprimento do seu produto: ')
                    if length == '':
                        pass
                    else:
                        self.list_products[index][index1+4][0] = length
                        pass
                    heigth = input('Digite a nova altura do produto: ')
                    if heigth== '':
                        pass
                    else:
                        self.list_products[index][index1+4][1] = heigth
                        pass
                    weigth = input('Digite a nova altura do produto: ')
                    if weigth == '':
                        pass
                    else:
                        self.list_products[index][index1+4][2] = weigth
                        pass
        else:
            print('')
            print('PRODUTO NÃO CADASTRADO!')
            print('')