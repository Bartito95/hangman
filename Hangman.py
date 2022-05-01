def insert_word():
    word = input("Please, insert a chosen word here: ").lower()
    forbidden_sign = {}
    for sign in "!@#$%^&*(){}:;',. _<>/?+1234567890":
        if sign in word:
            forbidden_sign[sign] = 1
        else:
            forbidden_sign[sign] = 0
    
    check_of_unwanted_signs = list(forbidden_sign.values())
    if 1 in check_of_unwanted_signs:
        forbidden_sign.clear
        return insert_word()
    else:
        return word


#convert a word into "_"
def floors(word):
    floors = []
    for w in word:
        if w == "-":
            w = w
            floors.append(w)
        else:
            w = "_"    
            floors.append(w)
    return "".join(floors)


def find_all_occur(letter, word):
    indexes = []
    for occ in enumerate(word):
        if occ[1] == letter:
            indexes.append(occ[0])
    return indexes

def letter():
    let = str(input("Insert a letter: ").lower())
    if let.isalpha():
        if len(let) == 1:
            return let
        else:
            print("Wrong, repeat!\n")
            return letter()
    else:
        print("Wrong, repeat!\n")
        return letter()
    
def game():
    word = insert_word()
    print()
    empty = floors(word)
    print()
    loose = 0
    used_letters = []
    correct_letters = []
    wrong_letters = []
    
    while loose < 3:
        print()
        let = letter()
        print()
            
        if let in word:
            if let not in used_letters:
                occurances = find_all_occur(let, word)
                for l in occurances:
                    empty = list(empty)
                    empty[l] = let
                    empty = "".join(empty)
                    used_letters.append(let)
                    correct_letters.append(let)
                print(empty)
                print()
                if word == empty:
                    return "Congrats, you won!"
                else:
                    print("You have used those letters: {}".format(set(used_letters)))
                    print("Letters correct: {}".format(set(correct_letters)))
                
            else:
                print("You have already used that letter!")
                continue
        else:
            if let not in used_letters:
                loose += 1
                used_letters.append(let)
                wrong_letters.append(let)
                print("You have used those letters: {}".format(set(used_letters)))
                print("\nWrong letters: {}".format(set(wrong_letters)))
                print("\nYou have used {} chances out of 3\n".format(loose))
                print()
                print(empty)
                

                if loose == 3:
                    print()
                    return "Unfortunately, you have lost."
            
            else:
                print("\nYou have used that letter!")
                continue

            
        
print(game())