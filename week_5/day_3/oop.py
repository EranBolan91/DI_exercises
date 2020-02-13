class Writer:

    def __init__(self, name, n_books, genre):
        self.name = name
        self.n_books = n_books
        self.genre = genre

    def write(self):
        self.n_books += 1
        print(f"{self.name} wrote a book")

    @staticmethod
    def say_hi():
        print("Hi !")


class Philosopher(Writer):

    def __init__(self, name, n_books, genre, domain):
        super().__init__(name, n_books, genre)
        self.domain = domain

    def write_nonsense(self):
        self.n_books += 1
        print(f"{self.name}: What is this nonsense")


class French:

    def __init__(self, name):
        self.name = name

    def talk_nonsense(self):
        print(f"{self.name}: bla bla...nonsense...bla bla")


class FrenchPhilosopher(Philosopher, French):

    def conference(self):
        print(f"{self.name}: ...Post Modern nonsense...")


if __name__ == '__main__':
    albert = Writer(name="Albert Camus", n_books=25, genre=["Philosophy", "Roman"])
    print(albert.name)
    print(albert.n_books)
    print(albert.genre)

    albert.write()
    print(albert.n_books)
    albert.say_hi()

    fred = Philosopher("Freidrich", 30, ["Amoralism", "Uberstuff"], domain="Philology")

    print(fred.n_books)
    fred.write()
    print(fred.n_books)

    fred.write_nonsense()
    print(fred.n_books)

    derrida = FrenchPhilosopher(name="Jacques Derrida", n_books=100, genre=["Post Modernism", "Philology"],
                                domain="Linguistics")

    derrida.conference()  # frenchphilo
    derrida.talk_nonsense()  # French
    derrida.write()  # writer
    derrida.write_nonsense()  # Philosopher
