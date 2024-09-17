import random
import csv

class Casino:
    __MAX_TURNS = 20
    __MAX_BET_AMOUNT = 1000
    __WIN_MULTIPLIER = 10
    __VALID_BET_NUMBERS = [1,2,3,4,5,6,7,8,9]
    __CSV_FILENAME = "gegevens.csv"

    def get_max_turns(self):
        return self.__MAX_TURNS
    
    def get_max_bet_amount(self):
        return self.__MAX_BET_AMOUNT

    def get_valid_bet_numbers(self):
        return self.__VALID_BET_NUMBERS

    def get_winning_number(self):
        return 1
        return random.randint(0, 10)
    
    def apply_win_multiplier(self, amount):
        return amount * self.__WIN_MULTIPLIER

    def schrijfnaarcsv(self, coins : list):
        with open(self.__CSV_FILENAME, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(coins)
    
    def uitlezencsv(self):
        running_total = 0
        row_index = 0
        row_values = []
        # Open the CSV file
        with open(self.__CSV_FILENAME, 'r') as csvfile:
            reader = csv.reader(csvfile)
            for index, row in enumerate(reader):
                if index == row_index:
                    row_values = row
                break
            row_values = [int(item) for item in row_values]
            for val in row_values:
                running_total += val
        return running_total
    
    def show_result(self, win_loss : int):
        if win_loss > 0:
            print(f"Het casino heeft {win_loss} gewonnen")
        else:
            print(f"Het casino heeft {win_loss*-1} verloren")