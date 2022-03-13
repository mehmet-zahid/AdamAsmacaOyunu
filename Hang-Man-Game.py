# Created by Mehmet Zahid for educational purposes.


import time


#########################################################################################
# veriyi ekrana harf harf yazar.

def Write_Screen(line, delay=0.001):
    for i in range(len(line)):
        print(line[i], end='', flush=True)
        time.sleep(delay)
    print("\n")


############################################################################################

# program ana menu
def Main_Display():
    symbol = "_" * 80

    Title = "Welcome to play HANGMAN Game"
    Description = "Description: Type a 'letter' to guess the secret word."

    # for i in range(80):
    #     print(symbol,end='',flush=True)
    #     time.sleep(0.01)
    # print("\n")
    # for i in range(len(Title)):
    #     print(Title[i],end='',flush=True)
    #     time.sleep(delay)
    Write_Screen(symbol, delay=0.001)
    Write_Screen(Title)
    Write_Screen(Description)
    Write_Screen(symbol, delay=0.001)


##################################################################################################

secret_word = "Power"
Right_Attempt_Count = 0
Trying_Limit = 10
Last_Chance = Trying_Limit
letter_index = []
Main_Display()

for i in range(len(secret_word)):
    print("*")

while True:
    # Attempt_Count +=1
    # if Attempt_Count==11:
    #     print(f"Last {Last_Chance} Chance!")
    #     print("You Failed ! Man died!")
    #     break
    if Last_Chance == 0:
        print("...GAME OVER...\nYou Failed!\nMan died!")
        break
    if Right_Attempt_Count == len(secret_word):
        print("You won!")
        break
    guessed_letter = input("Type a letter: ")

    print(f"You typed the letter: '{guessed_letter}'")
    Write_Screen("....", delay=0.005)

    if guessed_letter in secret_word:

        letter_index.append(secret_word.index(guessed_letter))
        guessed_letter = guessed_letter
        print(f"Last {Last_Chance} Chance!")
        print("Congratulations!")
        print(f"'{guessed_letter}' is true.")

        for i in range(len(secret_word)):
            if i == secret_word.index(guessed_letter):
                print(guessed_letter)

            elif i in letter_index:

                print(secret_word[i])

            else:
                print("*")

        Right_Attempt_Count += 1



    else:

        Last_Chance -= 1
        print("Sorry!")
        print(f"'{guessed_letter}' is not true.")
        print(f"Last {Last_Chance} Chance!")

        for i in range(len(secret_word)):

            if i in letter_index:

                print(secret_word[i])

            else:
                print("*")

