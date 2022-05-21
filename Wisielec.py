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

word = Choose_random_word()
dummy_word = []
#print(dummy_word)
for i in range(len(word)):
    dummy_word.append("_")

def Count_and_insert_correct_letters(letter):
    cnt = 0
    for i in range(len(word)):
        if(word[i]==letter):
            dummy_word[i] = letter
            cnt += 1
    return cnt

count_correct_letters = 0
chances_count = 9
input_letters_list = []
while True:
    if(count_correct_letters == len(word)):
        print(*dummy_word)
        print("Congratulations, you may just will have been winning!")
        break
    if(chances_count == 0):
        print(*dummy_word)
        print("LOL, nice try bro, maybe next time you'll get there")
        break
    print("THE WORD TO GUESS")
    print(*dummy_word)
    print("You have " + str(chances_count) + " more chances")
    print("Enter a letter:")
    input_letter = input()
    if(input_letter in input_letters_list):
        print("Please do not write the same letter again")
        continue
    input_letters_list.append(input_letter)
    if input_letter in word:
        print("Good one")
        count_correct_letters += Count_and_insert_correct_letters(input_letter)
    else:
        print("Not this time")
        chances_count -= 1


