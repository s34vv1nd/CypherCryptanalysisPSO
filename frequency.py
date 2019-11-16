class Frequency:

    def __init__(self, n_gram, alphabet):
        self.n_gram = n_gram
        self.alphabet = alphabet
        # grams[i] is all string in i_gram
        # pos_of[i][s] is the position of s in gram[i]
        self.grams = [[] for _ in n_gram]
        self.pos_of = [dict() for _ in n_gram]
        for i in range(len(n_gram)):
            def add_grams(x, s):
                if x == n_gram[i]:
                    self.grams[i].append(s)
                    self.pos_of[i][s] = len(self.grams[i]) - 1
                    return
                for c in alphabet:
                    add_grams(x + 1, s + c)
            add_grams(0, "")
        self.ftab = []

    def get_frequency(self, text):
        appearance = calculate_appearance(text, self.alphabet, self.n_gram, self.grams, self.pos_of)
        self.ftab = frequency_table(appearance)

    def get_frequency_from_file(self, filename):
        appearance = []
        for i in range(len(self.n_gram)):
            f = open(filename[i], "r")
            text = f.read()
            text = list(text.split())
            appearance.append([0 for _ in self.grams[i]])
            for j in range(0, len(text) - 1, 2):
                appearance[i][self.pos_of[i][text[j]]] = int(text[j + 1])
        self.ftab = frequency_table(appearance)


def calculate_appearance(text, alphabet, n_gram, grams, pos_of):
    text = plaintext(text, alphabet)
    appearance = []
    for i in range(len(n_gram)):
        appearance.append([0 for _ in grams[i]])
        for j in range(len(text) - n_gram[i]):
            t = text[j:j + n_gram[i]]
            appearance[i][pos_of[i][t]] += 1
    return appearance


def frequency_table(appearance):
    ftab = appearance
    for i in range(len(appearance)):
        total = sum(appearance[i])
        for j in range(len(appearance[i])):
            ftab[i][j] = appearance[i][j] / total
    return ftab


def plaintext(text, alphabet):
    text = "".join(c.upper() for c in text if c.upper() in alphabet)
    return text
