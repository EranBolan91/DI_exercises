class Text:
    def __init__(self,text):
        self.text = text.lower()

    @classmethod
    def from_file(cls,filepath):
        file = open(filepath,'r')
        readFile = file.read()
        file.close()
        return cls(readFile)


    def frequency(self):
        self.textDir = {}
        cleanText = self.cleanText(self.text)
        splitText = cleanText.split()
        for word in splitText:
            if word in self.textDir.keys():
                self.textDir[word] += 1
            else:
                self.textDir[word] = 1

        if self.textDir == "":
            return None
        else:
            message = """"""
            for key,value in self.textDir.items():
                message += f"{key}: {value} \n"
            return message


    def cleanText(self,text):
        for chr in self.text:
            if chr == ".":
                self.text = self.text.replace(chr,"")
            elif chr == ";":
                self.text = self.text.replace(chr, "")
            elif chr == ",":
                self.text = self.text.replace(chr, "")
            elif chr == ":":
                self.text = self.text.replace(chr, "")
            elif chr == "'":
                self.text = self.text.replace(chr, "")
        return self.text

    def commonWord(self):
        common = 0
        common_word = ""
        for word,count in self.textDir.items():
            if common < count:
                common = count
                common_word = word
        return common_word

    def uniqueWords(self):
        uniqueList = []
        for word,count in self.textDir.items():
            if count == 1:
                uniqueList.append(word)
        return uniqueList

#text = Text("MOTHER died today. Or, maybe, yesterday; I can't be sure. The telegram from the Home says: YOUR MOTHER PASSED AWAY. FUNERAL TOMORROW. DEEP SYMPATHY. Which leaves the matter doubtful; it could have been yesterday.")
text = Text.from_file("my_file.txt")
text.frequency()
print(text.commonWord())
print(text.uniqueWords())