import random
word_list =             ["abomination",
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
dummy_list = []
for i in range(len(word)):
    dummy_list.append('_')

def Right_letter(letter):
    for i in range(len(word)):
        if(word[i]==letter):
            dummy_list[i] = letter



