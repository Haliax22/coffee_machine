# Write your code here
class CoffeeMachine:
    def __init__(self, cwater, cmilk, cbeans, ccups, cmoney):
        self.cwater = cwater
        self.cmilk = cmilk
        self.cbeans = cbeans
        self.ccups = ccups
        self.cmoney = cmoney
        self.process_method()

    def UI_method(self):
        return input()

    def fbuy(self):
        print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
        command = self.UI_method()
        if command == '1':
            water, beans, cost = self.espresso()
            if self.cwater - water >= 0 and self.cbeans - beans >= 0 and self.ccups - 1 >= 0:
                self.cwater = self.cwater - water
                self.cbeans = self.cbeans - beans
                self.ccups = self.ccups - 1
                self.cmoney = self.cmoney + cost
                print('I have enough resources, making you a coffee!')
                self.process_method()
            else:
                if self.cwater - water < 0:
                    print('Sorry, not enough water!')
                    self.process_method()
                if self.cbeans - beans < 0:
                    print('Sorry, not enough coffee beans!')
                    self.process_method()
                if self.ccups - 1 < 0:
                    print('Sorry, not enough disposable cups!')
                    self.process_method()

        elif command == '2':
            water, milk, beans, cost = self.latte()
            if self.cwater - water >= 0 and self.cbeans - beans >= 0 and self.ccups - 1 >= 0 and self.cmilk - milk >= 0:
                self.cwater = self.cwater - water
                self.cmilk = self.cmilk - milk
                self.cbeans = self.cbeans - beans
                self.ccups = self.ccups - 1
                self.cmoney = self.cmoney + cost
                print('I have enough resources, making you a coffee!')
                self.process_method()
            else:
                if self.cwater - water < 0:
                    print('Sorry, not enough water!')
                    self.process_method()
                elif self.cbeans - beans < 0:
                    print('Sorry, not enough coffee beans!')
                    self.process_method()
                elif self.ccups - 1 < 0:
                    print('Sorry, not enough disposable cups!')
                    self.process_method()
                elif self.cmilk - milk < 0:
                    print('Sorry, not enough milk!')
                    self.process_method()

        elif command == '3':
            water, milk, beans, cost = self.cappuccino()
            if self.cwater - water >= 0 and self.cbeans - beans >= 0 and self.ccups - 1 >= 0 and self.cmilk - milk >= 0:
                self.cwater = self.cwater - water
                self.cmilk = self.cmilk - milk
                self.cbeans = self.cbeans - beans
                self.ccups = self.ccups - 1
                self.cmoney = self.cmoney + cost
                print('I have enough resources, making you a coffee!')
                self.process_method()
            else:
                if self.cwater - water < 0:
                    print('Sorry, not enough water!')
                elif self.cbeans - beans < 0:
                    print('Sorry, not enough coffee beans!')
                elif self.ccups - 1 < 0:
                    print('Sorry, not enough disposable cups!')
                elif self.cmilk - milk < 0:
                    print('Sorry, not enough milk!')
                self.process_method()
        elif command == 'back':
            self.process_method()

    def espresso(self):
        water = 250
        beans = 16
        cost = 4
        return water, beans, cost

    def latte(self):
        water = 350
        milk = 75
        beans = 20
        cost = 7
        return water, milk, beans, cost

    def cappuccino(self):
        water = 200
        milk = 100
        beans = 12
        cost = 6
        return water, milk, beans, cost


    def f_fill(self):
        print('Write how many ml of water do you want to add:')
        water = int(self.UI_method())
        print('Write how many ml of milk do you want to add:')
        milk = int(self.UI_method())
        print('Write how many grams of coffee beans do you want to add:')
        beans = int(self.UI_method())
        print('Write how many disposable cups do you want to add:')
        cups = int(self.UI_method())
        self.cwater = self.cwater + water
        self.cmilk = self.cmilk + milk
        self.cbeans = self.cbeans + beans
        self.ccups = self.ccups + cups
        self.process_method()


    def f_take(self):
        print('I gave you $' + str(self.cmoney))
        self.cmoney = 0
        self.process_method()


    def current_status(self):
        print('The coffee machine has:')
        print(str(self.cwater) + ' of water')
        print(str(self.cmilk) + ' of milk')
        print(str(self.cbeans) + ' of coffee beans')
        print(str(self.ccups) + ' of disposable cups')
        print(str(self.cmoney) + ' of money')
        self.process_method()

    def process_method(self):
        print('Write action (buy, fill, take, remaining, exit):')
        action = self.UI_method()
        if action == 'buy':
            self.fbuy()
        elif action == 'fill':
            self.f_fill()
        elif action == 'take':
            self.f_take()
        elif action == 'remaining':
            self.current_status()
        elif action == 'exit':
            return None

coffee_machine = CoffeeMachine(400, 540, 120, 9, 550)
