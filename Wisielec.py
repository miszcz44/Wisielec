import random
word_list = ["abomination",
             "cruelty",
             "verification",
             "possibility",
             "investing",
             "cucumber",
             "intendation",
             "graduation",
             "zombie",
             "postromanticism"]


def Choose_random_word():
    return random.choice(word_list)

def Count_and_insert_correct_letters(letter):
    cnt = 0
    for i in range(len(word)):
        if(word[i]==letter):
            dummy_word[i] = letter
            cnt += 1
    return cnt

def Ask_for_another_game():
    print("Wanna play again?(y/n)")
    return input()



flag = True
while flag:
    count_correct_letters = 0
    chances_count = 9
    input_letters_list = []
    word = Choose_random_word()
    dummy_word = []
    for i in range(len(word)):
        dummy_word.append("_")
    while flag:
        if(count_correct_letters == len(word) or chances_count == 0):
            print(*dummy_word)
            if(count_correct_letters == len(word)):
                print("Congratulations, you may just will have been winning!\n")
            else:
                print("LOL, nice try bro, maybe next time you'll get there\n")
            another_game_choice = Ask_for_another_game()
            if(another_game_choice == "y" or another_game_choice == "Y"):
                word_list.remove(word)
                break
            elif(another_game_choice == "n" or another_game_choice == "N"):
                flag = False
                break

        print("THE WORD TO GUESS")
        print(*dummy_word)
        print("You have " + str(chances_count) + " more chances")
        print("Enter a letter:")
        input_letter = input()
        input_letter = input_letter.lower()
        while(input_letter.isalpha() == False or input_letter in input_letters_list or len(input_letter)>1):
            if(len(input_letter)>1):
                print("Just one letter will be enough, trust me")
            if(input_letter.isalpha() == False):
                print("Please enter an english alphabet letter")
                input_letter = input()
            if(input_letter in input_letters_list):
                print("Please do not write the same letter again")
                input_letter = input()
        input_letters_list.append(input_letter)
        if input_letter in word:
            print("Good one")
            count_correct_letters += Count_and_insert_correct_letters(input_letter)
        else:
            print("Not this time")
            chances_count -= 1


