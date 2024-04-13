from models.transaction import Transaction

class Initialize():

		def show_menu(self):
				print(50 * '-')
				print("Bem-vindo ao Controle Financeiro")
				print(50 * '-')

				print("1. Adicionar Transação")
				print("2. Ver Transações")
				print("3. Sair")

		def choose_option(self):
				option = input("\nEscolha uma opção: ")

				if option not in ['1', '2', '3']:
						print("\nOpção inválida")

				return option

		def to_add(self):
				operation = input("Informe o tipo da operação: ")
				value = input("Informe o valor da operação: ")
				description = input("Informe a descrição da operação: ")

				transaction = Transaction(operation, value, description)

				transaction.save()

				del transaction


		def to_view(self):
				Transaction().view()

		def to_exit(self):
				print("\nObrigado, até mais!")
				exit()


if __name__ == '__main__':
		init = Initialize()
		option = ''

		while option !='3':
				init.show_menu()
				option = init.choose_option()

				if option == '1':
						init.to_add()
				elif option == '2':
						init.to_view()
				elif option == '3':
						init.to_exit()