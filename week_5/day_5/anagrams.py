from anagram_checker import AnagramChecker
anagram = AnagramChecker()
while exit:
    menu = """
    (i) New word
    (x) Exit
    """
    print(menu)
    user_input = input("Please choose: ")
    if user_input == "i" or user_input == "I":
        word_checker = True
        while word_checker:
            user_word = input("Please enter your word ")
            arr_word = user_word.split(" ")
            isDigit = any(char.isdigit() for char in user_word)
            if len(arr_word) > 1 or isDigit:
                print("Please enter only one alphabet word")
            else:
              anagram_list = anagram.is_valid_word(user_word)
              anagram.message_print(anagram_list,user_word)
              break
    else:
        print("Bye bye")
        break





