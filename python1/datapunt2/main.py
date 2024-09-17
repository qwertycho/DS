#!/usr/bin/python3
import user as User
import casino as Casino

# twee classes gemaakt om bepaalde functionaliteit te groeperen en main.py simpel te houden
casino = Casino.Casino()
user = User.User()

def main():
    #alle in en uitgaande bedragen bijhouden om later weg te schrijven naar de csv
    history = []

    for turn in range(casino.get_max_turns()):
        #als eerste controleren of de user wel in staat is om te spelen
        if user.get_capital() <= 0:
            print(f"u heeft geen coins meer!")
            casino.schrijfnaarcsv(history)
            return 
        
        #vragen of de gebruiker door wilt gaan.
        #dit komt na de capital check om te voorkomen dat de gebruiker eerst door wilt gaan en dat niet verder kan spelen
        #alleen wanneer de user al 1 ronde heeft gespeeld vragen of hij verder wilt gaan
        if turn > 0:
            while True:
                cont = input("wil je doorgaan [y, n] ")
                if cont == 'n':
                    print("Bedankt voor het spelen en tot ziens")
                    casino.schrijfnaarcsv(history)
                    return 
                elif cont == 'y':
                    break
            
        bet_amount = user.Get_bet_amount()

        user_bet = user.Get_bet_number(casino.get_valid_bet_numbers())
        winning_number = casino.get_winning_number()

        if user_bet == winning_number:
            win_amount = casino.apply_win_multiplier(bet_amount)
            user.add_capital(win_amount)
            history.append(-win_amount)
            print(f"inzet is verdubbeld, je hebt nu {user.get_capital()}")
        else:
            user.subtract_capital(bet_amount)
            history.append(bet_amount)
            print("inzet is helaas verloren")

    casino.schrijfnaarcsv(history)

main()
win_loss = casino.uitlezencsv()
casino.show_result(win_loss)