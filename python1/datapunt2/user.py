class User:
    '''
    class voor het bijhouden van kapitaal
    '''
    ___MAX_BET_AMOUNT = 1000
    __capital = 1000

    def Get_bet_amount(self):
        '''
        Returns the amount the user wants to bet.
        This value is NOT removed from the user's capital
        '''
        while True:
            #voorkomen dat deze functie in een loop blijft wanneer de user geen capital meer heeft
            if self.__capital <= 0:
                raise Exception("no capital")
                
            try:
                bet = int(input("Hoeveel coins wil je inzetten: "))
            except:
                print("Geen geldige hoeveelheid coins!")

            if bet > self.__capital or bet > self.___MAX_BET_AMOUNT:
                #waarschuwing dat het bedrag te hoog is
                #ternary om te bepalen of het maximum bedrag de maximale inzet of de user's capitaal is
                print(f"inzet te hoog, u mag maximaal {self.__capital if self.__capital < self.___MAX_BET_AMOUNT else self.___MAX_BET_AMOUNT } inzetten")
            elif bet <= 0:
                print("Geen geldige hoeveelheid coins!")
            else:
                return bet

    def Get_bet_number(self, allowed : list):
        '''
        Get the number the user wants to bet on.
        allowed is a list containing all the valid betting numbers
        '''
        while True:
            try:   
                number = int(input("Op welk getal wil je gokken (1-9): "))
                if number in allowed:
                    return number
            except:
                # kwaadaardige lege except om int conversie te vangen
                pass
            print("je mag alleen hele getallen van 1 tot 9 invullen")

    def add_capital(self, amount : int):
        if amount < 1:
            raise Exception("invalid amount")
        
        self.__capital += amount
    
    def subtract_capital(self, amount : int):
        if amount < 1:
            raise Exception("invalid amount")
        self.__capital -= amount
    
    def get_capital(self):
        return self.__capital