class Book:

    def __init__(self, title, author, text):
        self.title = title
        self.author = author
        self.text = text
        self.sentences = self.text.split('. ')

    def __repr__(self):
        return f'Book: {self.title} by {self.author}'

    def __add__(self, other):
        return Book(title=self.title + ' & ' + other.title,
                    author=self.author + ' & ' + other.author,
                    text=self.text + '\n' + other.text)

    def __len__(self):
        return len(self.text)

    def __mul__(self, other):
        if type(other) == int:
            return [self] * other
        elif isinstance(other, Book):
            return [self] * len(other)
        else:
            raise TypeError('Unsupported operation')

    def __gt__(self, other):
        if isinstance(other, Book):
            return len(self) > len(other)
        else:
            raise TypeError('Unsupported operation')

    def __lt__(self, other):
        if isinstance(other, Book):
            return len(self) < len(other)
        else:
            raise TypeError('Unsupported operation')

    def __getitem__(self, item):
        return self.sentences[item]

    # def __iter__(self):
    #     self.i = 0
    #     return self
    #
    # def __next__(self):
    #     if self.i >= len(self.sentences):
    #         raise StopIteration
    #     else:
    #         out = self.sentences[self.i]
    #         self.i += 1
    #         return out


if __name__ == '__main__':
    zohar = Book(title='The Zohar', author='Rabbi Shimon bar Yohai', text="hbckhjzdc. zhjcbkjdbchz. sjkzcbhzjkhbcd. ")
    lotr = Book(title='Lord of the Rings',
                author='JR Tolkien', text='......')

    print(zohar)
    print(zohar + lotr)
    zohar.__add__(lotr)
    print(zohar * 3)
    print(type(zohar))
    print(zohar * lotr)

    print(zohar > lotr)
    print(zohar < lotr)

    for something in zohar:
        print(something)

    print(zohar[0])

    with open("the_stranger.txt", "r") as file:
        text = file.read()

    with open("my_book.txt", "w") as file:
        file.write(text)

    stranger = Book(title='the stranger', author='Albert Camus',
                    text=text)

    print(stranger)
    for sentence in stranger:
        print(sentence)

    print(len(stranger))
