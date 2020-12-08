import os

class Categories:

    categories: list = [['eletronicos', 'celulares', 'caixas de son', 'games'], 
    ['livros', 'scifi', 'drama', 'biografias'], ['música','cds','discos'], 
    ['móveis e decoração','mesas','cadeidas','sofas'], ['papelaria', 'cadernos','canetas'], 
    ['petshop','coleiras', 'ração']]
    

    def categories_menu(self) -> int:

        print('')
        print("CATEGORIAS CADASTRADAS:")
        print('')    
        for j in self.categories:
            for i in range(len(j)):
                if i == 0:
                    print('')
                    print(j[i])
                else:
                    print('     '+str(j[i]))
                    
        print('')
        print('1 - Consultar e adicionar nova categoria')
        print('2 - Editar categoria')
        print('0 - Sair')
        print('')
        self.option = input('Digite a opção escolhida (use os números): -> ')
        return self.option

    def add(self):
        name = input("Digite o nome da nova categoria:  ")

        if any(name in list for list in self.categories):
            print('')
            print('A CATEGORIA JÁ EXISTE!')
            print('')
            pass   
        else:
            self.categories.append([name])
            print('')
            print('CATEGORIA ADICIONADA!')
            print('')
            print('Gostaria de adicionar uma subcategoria?')
            print('1 - SIM')
            print('2 - NÃO')
            sub = input('Use os números ->')

            if sub == '1':
                subcategorie = input('Digite o nome da nova subcategoria: ')
                if any(subcategorie in list for list in self.categories):
                    print('')
                    print('A CATEGORIA JÁ EXISTE!')
                    print('')
                    pass 
                else:
                    self.categories[len(self.categories)-1].append(subcategorie)
                    pass
            else:
                os.system('clear') 
                pass     
            pass
            

    def edit(self):
        element = input("Digite o nome da categoria que deseja editar:  ")

        if any(element in list for list in self.categories):
            index = [i for i, j in enumerate(self.categories) if element in j][0]
            index1 = self.categories[index].index(element)
            name = input('Digite o novo nome da categoria: ')
            if name == '':
                pass
            else:
                if any(name in list for list in self.categories):
                    print('')
                    print('CATEGORIA JÁ EXISTE!')
                    print('')
                    pass
                else:
                    self.categories[index][index1] = name
                    print('')
                    print('CATEGORIA MODIFICADA COM SUCESSO!')
                    print('')
                    pass
            pass   
        else:
            self.categories.append([name])
            print('')
            print('CATEGORIA NÃO CADASTRADA')
            print('')
            pass

    def delete(self):
        print('')
        element = input('Digite o nome da categoria que deseja excluir: ')
        if any(element in list for list in self.categories):
            index = [i for i, j in enumerate(self.categories) if element in j][0] 
            self.categories.pop(index)
            print('')
            print('CATEGORIA EXCLUIDA!')
            print('')
            pass
        else:
            print('')
            print('CATEGORIA NÃO CADASTRADA!')
            print('') 


