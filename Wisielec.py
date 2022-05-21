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
while(count_correct_letters<len(word)):
    print(*dummy_word)
    print("Enter a letter:")
    input_letter = input()
    if input_letter in word: count_correct_letters += Count_and_insert_correct_letters(input_letter)


