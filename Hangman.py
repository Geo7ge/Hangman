import random

def draw(case_number):
    if case_number == 0:
        print()
        print("  ------------")
        print("  |          |")
        print("  |           ")
        print("  |")
        print("  |")
        print("  |")
        print("  |")
        print("------   ", end = "")
        for i in range(len(word)):
            if word[i] in used_letters :
                print(word[i], end = " ")
            else:
                print("_", end = " ")
            
        print()
        print()
        print()
        
    if case_number == 1:
        print()
        print("  ------------")
        print("  |          |")
        print("  |          O ")
        print("  |")
        print("  |")
        print("  |")
        print("  |")
        print("------   ", end = "")
        for i in range(len(word)):
            if word[i] in used_letters :
                print(word[i], end = " ")
            else:
                print("_", end = " ")
            
        print()
        print()
        print()
        
    if case_number == 2:
        print()
        print("  ------------")
        print("  |          |")
        print("  |          O")
        print("  |          |")
        print("  |")
        print("  |")
        print("  |")
        print("------   ", end = "")
        for i in range(len(word)):
            if word[i] in used_letters :
                print(word[i], end = " ")
            else:
                print("_", end = " ")
            
        print()
        print()
        print()
        
    if case_number == 3:
        print()
        print("  ------------")
        print("  |          |")
        print("  |          O")
        print("  |         \|")
        print("  |")
        print("  |")
        print("  |")
        print("------   ", end = "")
        for i in range(len(word)):
            if word[i] in used_letters :
                print(word[i], end = " ")
            else:
                print("_", end = " ")
            
        print()
        print()
        print()
        
    if case_number == 4:
        print()
        print("  ------------")
        print("  |          |")
        print("  |          O ")
        print("  |         \|/")
        print("  |")
        print("  |")
        print("  |")
        print("------   ", end = "")
        for i in range(len(word)):
            if word[i] in used_letters :
                print(word[i], end = " ")
            else:
                print("_", end = " ")
            
        print()
        print()
        print()
        
    if case_number == 5:
        print()
        print("  ------------")
        print("  |          |")
        print("  |          O")
        print("  |         \|/")
        print("  |          /")
        print("  |")
        print("  |")
        print("------   ", end = "")
        for i in range(len(word)):
            if word[i] in used_letters:
                print(word[i], end = " ")
            else:
                print("_", end = " ")
            
        print()
        print()
        print()

    if case_number == 6:
        print()
        print("  ------------")
        print("  |          |")
        print("  |          O")
        print("  |         \|/")
        print("  |          /\\")
        print("  |")
        print("  |")
        print("------   ", end = "")
        for i in range(len(word)):
            if word[i] in used_letters:
                print(word[i], end = " ")
            else:
                print("_", end = " ")
            
        print()
        print()
        print()


words = ("pisica", "caine", "dinozaur", "cal", "palat", "castel", "bunic", "banana", "piersica", "ananas", "cantar", "penar", "stilou", "pix", "radiera")
word = words[random.randint(0,len(words)-1)]
used_letters = []
used_letters.append(str(word[0]))
case_number = 0

while(True):
    draw(case_number)
    letter = input("Introduceti o letter : ")
    used_letters.append(letter)
    print()
    print("Used letters were : ", *used_letters)
    print()
    if letter in word:
        print("letter right")
    else:
        print("letter wrong")
        case_number += 1
    for j in range(len(word)):
        if word[j] in used_letters:
            if j == len(word)-1:
                print("---YOU WON---")
                break
    if word[j] in used_letters:
        if j == len(word)-1:
            break
    if case_number == 6:
        draw(case_number)
        print()
        print("---YOU LOST---")
        print()
        print("wordul WAS : ", word)
        break
        

