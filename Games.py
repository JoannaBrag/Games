import random

menu = input("Witaj! \nMam dla Ciebie trzy gry:\n1. Bulls and Cows\n2. Roll a dice \n3. Rock paper scissors\n\nW co chciałbyś zagrać? (Podaj numer gry): ")
print(menu)

if menu == "1":    # Bulls and Cows
    number = []
    attempts = 0
    print("System wybierze losowy numer. Twoim zadaniem jest podawać numery, aż zgadniesz co wymyślił system.\nBulls - udało Ci się zgadnąć dobrze pozycje. \nCows - udało Ci się zgadnąć dobrze liczbę/y.")

    def maszyna_losująca():
        for i in range(4):
            comp_number = random.randrange(0, 9)
            number.append(comp_number)

        if len(number) > len(set(number)):  #wskazuje, że w liście jest duplikat
            number.clear()      #usuwa listę, ponieważ pojawił się duplikat
            maszyna_losująca()  # zaczyna od nowa, szuka listy bez duplikatów

    def user():
        global attempts
        attempts += 1
        bulls = 0
        cows = 0
        print(number)
        user_input = input("Podaj 4 liczby: ")
        guess = []
        for i in range(4):
            guess.append(int(user_input[i]))
        for i in range(4):
            for j in range(4):
                if guess[i] == number[j]:
                    cows += 1
        for x in range(4):
            if guess[x] == number[x]:
                bulls += 1
        print("Bulls: ", bulls)
        print("Cows: ", cows)
        if (bulls == 4):
            print("Wygrałeś po tylu: ", attempts, "próbach")
        elif (bulls != 4):
            user()

    maszyna_losująca()
    user()

elif menu == "2":    #Roll a dice

    print("Zaczynamy grę! Roll a dice")

    def rolladice(roll):
        for i in range(0, roll):
            dice = random.randint(0, 6)
            print(dice)
        game_menu()

    def game_menu():
        print("1. Roll a dice")
        print("2. Roll multiple")
        print("3. Exit")
        choice = int(input("Wskaż, co chcesz robić: "))
        if choice == 1:
            rolladice(1)
        if choice == 2:
            roll = int(input("Ile razy?: "))
            rolladice(roll)
        if choice == 3:
            exit()
    game_menu()

elif menu == "3":   #Rock paper scissors
    print("Witaj w Rock paper scissors")

    count = 0

    while True:
        my_choice = input("My choice is: ").lower()
        print(my_choice)
        choices = ["rock", "scissors", "paper"]
        computer = random.choice(choices)
        print("Computer choice: ", computer)
        choice_dict = {"rock" : 0, "scissors" : 1, "paper" : 2}
        choice_index = choice_dict.get(my_choice, 3)
        computer_index = choice_dict.get(computer)
        # print(choice_index)

        result = [[0, 2, 1],
                  [1, 0, 2],
                  [2, 1, 0],
                  [3, 3, 3]]
        result_index = result[choice_index][computer_index]
        result_message = ["Szorstko", "You win", "You lose"]
        koniec = result_message[result_index]
        print(koniec)



    # Familiada
    import random

    lista = []
    occure = {}


    def familiada():
        computer = open("Nowy.txt", "r")
        for line in computer:
            s = (line.split(" "))
            for i in s:
                lista.append(i)
            choice = random.choice(lista)
        for i in choice:
            occure[i] = occure.get(i, 0) + 1
            # print(i, ": ", occure[i])


    def user():
        count = 0
        user_input = input("Zgadnij literę: ")
        if user_input in occure:
            print(("Bardzo dobrze. Litera {} zawiera się w słowie {} razy").format(user_input, occure[user_input]))
            count = count + 1

        if user_input not in occure:
            print("Nie ma tej litery w słowie. Próbuj dalej")
        user()


    familiada()
    user()
menu()