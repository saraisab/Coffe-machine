class CoffeeMachine:
    def __init__(self):
        self.ingredients = ['water', 'milk', 'beans', 'disposable_cups', 'money']
        self.initial = [400, 540, 120, 9, 550]
        self.buy_coffee()

    def print_content(self):
        print('\nThe coffee machine has:')
        print('{0} ml of water'.format(self.initial[0]))
        print('{0} ml of milk'.format(self.initial[1]))
        print('{0} g of coffee beans'.format(self.initial[2]))
        print('{0} disposable cups'.format(self.initial[3]))
        print('${0} of money\n'.format(abs(self.initial[4])))

    def buy_product(self, option):
        expresso = [-250, 0, -16, -1, 4]
        latte = [-350, -75, -20, -1, 7]
        capuccino = [-200, -100, -12, -1, 6]
        if option == '1':
            initial = [x + y for x, y in zip(self.initial, expresso)]
        elif option == '2':
            initial = [x + y for x, y in zip(self.initial, latte)]
        elif option == '3':
            initial = [x + y for x, y in zip(self.initial, capuccino)]
        j = 0
        contador = -1
        for i in initial:
            contador += 1
            if i <= 0:
                j += 1
                print(f'Sorry, not enough {self.ingredients[contador]}!\n')
                break
        if j == 0:
            print('I have enough resources, making you a coffee!\n')
            self.initial = initial

    def buy_coffee(self):
        action = 'buy'
        while action != 'exit':
            action = input('Write action (buy, fill, take, remaining, exit):\n')
            if action == 'buy':
                option = input('\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n')
                if option == 'back':
                    continue
                else:
                    self.buy_product(option)
            elif action == 'remaining':
                self.print_content()
            elif action == 'exit':
                exit()
            elif action == 'fill':
                print('')
                for a in range(len(self.initial)-1):
                    self.initial[a] += int(input(f'Write how many of {self.ingredients[a]} you want to add:\n'))
            elif action == 'take':
                print(f'I gave you ${self.initial[4]}\n')
                self.initial[4] = 0


if __name__ == '__main__':
    create_machine = CoffeeMachine()
