class AnagramChecker:
    def __init__(self):
        text = open("sowpods.txt","r")
        self.text_list = text.read().split('\n')

    def is_valid_word(self,word):
        word_list = set(self.text_list)
        if word.upper() in word_list:
            upper_word = word.upper()
            return self.get_anagrams(upper_word)


    def get_anagrams(self,word):
        anagram_words_list = []
        word_length = len(word)
        check_word = list(word)
        for char in check_word:
            for word_list in self.text_list:
                if char == word_list[0] and word_length == len(word_list):
                       if self.is_agaram(word,word_list,word_length):
                            anagram_words_list.append(word_list)
                       else:
                           continue
        return anagram_words_list


    def is_agaram(self,main_word,check_word,length):
        count = 0
        for char in main_word:
            if char in check_word:
                count += 1
        if count == length:
            return True
        else:
            return False

    def message_print(self,list,word):
        line = ""
        for word in list:
            line += word + ","
        print(f"Your word: {word}")
        print(f"this is a valid English word.")
        print(f"Anagrams for your word: {line}")